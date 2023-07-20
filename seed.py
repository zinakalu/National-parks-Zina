from models import db, User, Park
from faker import Faker
from config import app
from sqlalchemy.sql import func



fake = Faker()

parks = [
    {
        'name': 'Little River Canyon National Preserve',
        'location': 'Alabama',
        'activities': 'Hiking, Biking, Wildlife Viewing'
    },
    {
        'name': 'Denali National Park',
        'location': 'Alaska',
        'activities': 'Climbing, Hiking, Wildlife Tours',
        'campground': 'DeSoto State Park, Little River RV Park & Campground '
    },
    {
        'name': 'Grand Canyon National Park',
        'location': 'Arizona',
        'activities': 'Hiking, Rafting, Helicopter Tours',
        'campground': 'Mather Campground, Desert View Campground, North Rim Campground'
    },
    {
        'name': 'Trail of Tears National Historic Trail',
        'location': 'Arkansas',
        'activities': 'Hiking, Historical Tours',
        'campground': 'kjfslj'
    },
    {
        'name': 'Redwood National and State Parks',
        'location': 'California',
        'activities': 'Hiking, Wildlife Viewing, Biking',
        'campground': 'Jedediah Smith Campground, Mill Creek Campground'
    },
    {
        'name': 'Great Sand Dunes National Park & Preserve',
        'location': 'Colorado',
        'activities': 'Sandboarding, Hiking, Wildlife Viewing',
        'campground': 'Pinon Flats Campground'
    },
    {
        'name': 'Twin Brooks Park',
        'location': 'Connecticut',
        'activities': 'Picnicking, Playing Sports, Walking',
        'campground': 'dajhdjkj'
    },
    {
        'name': 'Chesapeake Bay Gateways and Watertrails Network',
        'location': 'Delaware',
        'activities': 'Boating, Fishing, Wildlife Viewing',
        'campground': 'jdlka'
    },
    {
        'name': 'Dry Tortugas National Park',
        'location': 'Florida',
        'activities': 'Snorkeling, Camping, Wildlife Viewing',
        'campground': 'Garden Key Campground'
    },
    {
        'name': 'Chattahoochee River National Recreation Area',
        'location': 'Georgia',
        'activities': 'Fishing, Hiking, Paddling',
        'campground': 'djhkf'
    },
    {
        'name': 'Kalaupapa National Historic Park',
        'location': 'Hawaii',
        'activities': 'Historical Tours, Hiking, Wildlife Viewing',
        'campground': 'ihodi'
    },
    {
        'name': 'Kalaupapa National Historic Park',
        'location': 'Hawaii',
        'activities': 'Historical Tours, Hiking, Wildlife Viewing',
        'campground': 'ihodi'
    }
    
]


with app.app_context():
    for _ in range(60):
        user = User(username=fake.user_name(), _password_hash=fake.password(), image_url=fake.url())
        db.session.add(user)
    db.session.commit()

    for park_info in parks:
        park = Park(name=park_info.get('name'),
                    location=park_info.get('location'),
                    activities=park_info.get('activities'),
                    campgrounds=park_info.get('campgrounds'),
                    user_id = User.query.order_by(func.random()).first().id)

        db.session.add(park)
    db.session.commit()


    