const form = document.getElementById("route-form");
const map = L.map("map").setView([60.25, 24.8], 11);
const API_URL = "https://api.digitransit.fi";
const DESTINATION = { lat: 60.22412, lon: 24.75873 }; // Karaportti 2
const HEADERS = { "Content-Type": "application/graphql", 'digitransit-subscription-key': '' };

L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

const routeLayer = L.layerGroup().addTo(map);

form.addEventListener("submit", async e => {
    e.preventDefault();
    const key = document.getElementById("key").value;
    HEADERS['digitransit-subscription-key'] = key;
    
    const { lat, lon } = await getCoordinates(document.getElementById("address").value);
    const route = await getRoute(lat, lon);
    displayRoute(route, { lat, lon });
});

const getCoordinates = async address => {
    const response = await fetch(`${API_URL}/geocoding/v1/search?text=${encodeURIComponent(address)}&size=1`, {
        method: "GET",
        headers: HEADERS
    });
    const { features: [{ geometry: { coordinates: [lon, lat] } }] } = await response.json();
    return { lat, lon };
};

const getRoute = async (lat, lon) => {
    const response = await fetch(`${API_URL}/routing/v2/finland/gtfs/v1`, {
        method: "POST",
        headers: HEADERS,
        body: `{ plan(from: {lat: ${lat}, lon: ${lon}}, to: {lat: ${DESTINATION.lat}, lon: ${DESTINATION.lon}}, numItineraries: 1) {
            itineraries { startTime endTime legs { mode legGeometry { points } } }
        }}`
    });
    return response.json();
};

const getColor = mode => ({
    WALK: 'green', BUS: 'red', RAIL: 'cyan', TRAM: 'magenta'
})[mode] || 'blue';

function displayRoute({ data: { plan: { itineraries: [itinerary] } } }, origin) {
    routeLayer.clearLayers();
    
    itinerary.legs.forEach(({ mode, legGeometry }) => {
        L.polyline(L.Polyline.fromEncoded(legGeometry.points).getLatLngs(), {
            color: getColor(mode)
        }).addTo(routeLayer);
    });

    map.fitBounds([[origin.lat, origin.lon], [DESTINATION.lat, DESTINATION.lon]]);
    
    const [start, end] = [itinerary.startTime, itinerary.endTime].map(t => new Date(t).toLocaleTimeString());
    document.getElementById("times").innerText = `Trip starts at ${start} and ends at ${end}`;
}