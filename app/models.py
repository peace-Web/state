from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATE_TYPE = [
    ("APT", "Appartement"),
    ("STR", "Store")
]

CITIES = [
    ('Casablanca', 'Casablanca'),
    ('Fez', 'Fez'),
    ('Tangier', 'Tangier'),
    ('Marrakesh', 'Marrakesh'),
    ('Salé', 'Salé'),
    ('Meknes', 'Meknes'),
    ('Rabat', 'Rabat'),
    ('Oujda', 'Oujda'),
    ('Kenitra', 'Kenitra'),
    ('Agadir', 'Agadir'),
    ('Tetouan', 'Tetouan'),
    ('Temara', 'Temara'),
    ('Safi', 'Safi'),
    ('Mohammedia', 'Mohammedia'),
    ('Khouribga', 'Khouribga'),
    ('El Jadida', 'El Jadida'),
    ('Beni Mellal', 'Beni Mellal'),
    ('Aït Melloul', 'Aït Melloul'),
    ('Nador', 'Nador'),
    ('Dar Bouazza', 'Dar Bouazza'),
    ('Taza', 'Taza'),
    ('Settat', 'Settat'),
    ('Berrechid', 'Berrechid'),
    ('Khemisset', 'Khemisset'),
    ('Inezgane', 'Inezgane'),
    ('Ksar El Kebir', 'Ksar El Kebir'),
    ('Larache', 'Larache'),
    ('Guelmim', 'Guelmim'),
    ('Khenifra', 'Khenifra'),
    ('Berkane', 'Berkane'),
    ('Taourirt', 'Taourirt'),
    ('Bouskoura', 'Bouskoura'),
    ('Fquih Ben Salah', 'Fquih Ben Salah'),
    ('Dcheira El Jihadia', 'Dcheira El Jihadia'),
    ('Oued Zem', 'Oued Zem'),
    ('El Kelaa Des Sraghna', 'El Kelaa Des Sraghna'),
    ('Sidi Slimane', 'Sidi Slimane'),
    ('Errachidia', 'Errachidia'),
    ('Guercif', 'Guercif'),
    ('Oulad Teima', 'Oulad Teima'),
    ('Ben Guerir', 'Ben Guerir'),
    ('Tifelt', 'Tifelt'),
    ('Lqliaa', 'Lqliaa'),
    ('Taroudant', 'Taroudant'),
    ('Sefrou', 'Sefrou'),
    ('Essaouira', 'Essaouira'),
    ('Fnideq', 'Fnideq'),
    ('Sidi Kacem', 'Sidi Kacem'),
    ('Tiznit', 'Tiznit'),
    ('Tan-Tan', 'Tan-Tan'),
    ('Ouarzazate', 'Ouarzazate'),
    ('Souk El Arbaa', 'Souk El Arbaa'),
    ('Youssoufia', 'Youssoufia'),
    ('Lahraouyine', 'Lahraouyine'),
    ('Martil', 'Martil'),
    ('Ain Harrouda', 'Ain Harrouda'),
    ('Suq as-Sabt Awlad an-Nama', 'Suq as-Sabt Awlad an-Nama'),
    ('Skhirat', 'Skhirat'),
    ('Ouazzane', 'Ouazzane'),
    ('Benslimane', 'Benslimane'),
    ('Al Hoceima', 'Al Hoceima'),
    ('Beni Ansar', 'Beni Ansar'),
    ("M'diq", "M'diq"),
    ('Sidi Bennour', 'Sidi Bennour'),
    ('Midelt', 'Midelt'),
    ('Azrou', 'Azrou'),
    ('Drargua', 'Drargua'),

]

NUMBER = [
    ('1e','premier'),
    ('2e','deuxième'),
    ('3e','troisième'),
    ('4e','quatrième'),
    ('5e','cinquième'),
    ('6e','sixième'),
]

PERIOD = [
    ('DAY', 'jour'),
    ('MONTH', 'mois')
]

STATUS = [
    ('Show', 'show'),
    ("Hide", 'hide')
]

class Renter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.PositiveIntegerField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to="profile_images",null=True, blank=True )

    def __str__(self) -> str:
        return self.user.username
    

class Appartement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    renter = models.ForeignKey(Renter, on_delete=models.CASCADE, null=True, blank=True)
    city = models.CharField(max_length=50, choices=CITIES)
    address = models.CharField(max_length=200)
    is_fork = models.BooleanField(blank=True, default=False)
    price = models.PositiveIntegerField(default=0.00)
    period = models.CharField(max_length=50, choices=PERIOD, default='mois')
    size = models.FloatField(default=0.00, help_text="size in M*M")
    tage = models.CharField(max_length=50, choices=NUMBER)
    rooms = models.PositiveIntegerField(default=0)
    bathroom = models.PositiveIntegerField(default=0)
    kitchen = models.PositiveIntegerField(default=0)
    image1 = models.ImageField( upload_to="apt-images", blank=True, null=True)
    image2 = models.ImageField(upload_to="apt-images", blank=True, null=True)
    image3 = models.ImageField(upload_to="apt-images", blank=True, null=True)
    image4 = models.ImageField(upload_to="apt-images", blank=True, null=True)
    image5 = models.ImageField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS, default='show', null=True)
    occupied = models.BooleanField(default=False, null=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self) -> str:
        return self.user.username
    
