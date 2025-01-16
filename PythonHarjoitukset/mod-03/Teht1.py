kuhan_pituus = float(input("Mikä on kuhasi pituus senttimetreinä? "))

if kuhan_pituus < 37:
    print(f"Kuha on liian lyhyt ja se on heitettävä takaisin järveen.")
    print(f"Kuhan on {kuhan_pituus} cm ja sen pitäisi olla {37-kuhan_pituus} cm pidempi!")
else:
    print(f"Saat pitää kuhasi!")