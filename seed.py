from models import db, User, Park
from faker import Faker
from config import app
from sqlalchemy.sql import func



fake = Faker()

parks = [
    {
        'name': 'Little River Canyon National Preserve',
        'location': 'Alabama',
        'activities': 'Hiking, Biking, Wildlife Viewing',
        'campground': '',
        'video': ''
    },
    {
        'name': 'Denali National Park',
        'location': 'Alaska',
        'activities': 'Climbing, Hiking, Wildlife Tours',
        'campground': 'DeSoto State Park, Little River RV Park & Campground ',
        'video': ''
    },
    {
        'name': 'Grand Canyon National Park',
        'location': 'Arizona',
        'activities': 'Hiking, Rafting, Helicopter Tours',
        'campground': 'Mather Campground, Desert View Campground, North Rim Campground',
        'video': ''
    },
    {
        'name': 'Trail of Tears National Historic Trail',
        'location': 'Arkansas',
        'activities': 'Hiking, Historical Tours',
        'campground': '',
        'video': ''
    },
    {
        'name': 'Redwood National and State Parks',
        'location': 'California',
        'activities': 'Hiking, Wildlife Viewing, Biking',
        'campground': 'Jedediah Smith Campground, Mill Creek Campground',
        'video': ''
    },
    {
        'name': 'Great Sand Dunes National Park & Preserve',
        'location': 'Colorado',
        'activities': 'Sandboarding, Hiking, Wildlife Viewing',
        'campground': 'Pinon Flats Campground',
        'video': ''
    },
    {
        'name': 'Twin Brooks Park',
        'location': 'Connecticut',
        'activities': 'Picnicking, Playing Sports, Walking',
        'campground': '',
        'video': ''
    },
    {
        'name': 'Chesapeake Bay Gateways and Watertrails Network',
        'location': 'Delaware',
        'activities': 'Boating, Fishing, Wildlife Viewing',
        'campground': '',
        'video': ''
    },
    {
        'name': 'Dry Tortugas National Park',
        'location': 'Florida',
        'activities': 'Snorkeling, Camping, Wildlife Viewing',
        'campground': 'Garden Key Campground',
        'video': ''
    },
    {
        'name': 'Chattahoochee River National Recreation Area',
        'location': 'Georgia',
        'activities': 'Fishing, Hiking, Paddling',
        'campground': '',
        'video': ''
    },
    {
        'name': 'Kalaupapa National Historic Park',
        'location': 'Hawaii',
        'activities': 'Historical Tours, Hiking, Wildlife Viewing',
        'campground': '',
        'video': ''
    },
    {
        'name': 'Yellowstone National Park',
        'location': 'Idaho',
        'activities': '',
        'campground': '',
        'video': ''
    },
    {
        'name': 'Mammoth Cave National Park',
        'location': 'Kentucky',
        'activities': '',
        'campground': '',
        'video': ''
    },
    {
        'name': 'Yellowstone National Park',
        'location': 'Idaho',
        'activities': '',
        'campground': '',
        'video': ''
    },
    {
        'name': 'Indiana Dunes National Park',
        'location': 'Indiana',
        'activities': '',
        'campground': '',
        'video': ''
    },
    {
        'name': 'Acadia National Park',
        'location': 'Maine',
        'activities': '',
        'campground': '',
        'video': ''
    },
    {
        'name': 'Isle Royale National Park',
        'location': 'Michigan',
        'activities': '',
        'campground': '',
        'video': ''
    },
    {
        'name': 'Voyageurs National Park',
        'location': 'Minnesota',
        'activities': '',
        'campground': '',
        'video': ''
    },
    {
        'name': 'Gateway Arch National Park',
        'location': 'Missouri',
        'activities': '',
        'campground': '',
        'video': ''
    },
    {
        'name': 'YellowStone National Park',
        'location': 'Montana',
        'activities': '',
        'campground': '',
        'video': ''
    },
    {
        'name': 'Death Valley National Park',
        'location': 'Nevada',
        'activities': '',
        'campground': '',
        'video': ''
    },
    {
        'name': 'White Sands National Park',
        'location': 'New Mexico',
        'activities': '',
        'campground': '',
        'video': ''
    },
    {
        'name': 'Theodore Roosevel National Park',
        'location': 'North Dakota',
        'activities': '',
        'campground': '',
        'video': ''
    },
    {
        'name': 'Great Smoky Mountains National Park',
        'location': 'North Carolina',
        'activities': '',
        'campground': '',
        'video': ''
    },
    {
        'name': 'Cuyahoga Valley National Park',
        'location': 'Ohio',
        'activities': '',
        'campground': '',
        'video': ''
    },
    {
        'name': 'Crater Lake National Park',
        'location': 'Oregon',
        'activities': '',
        'campground': '',
        'video': ''
    },
    {
        'name': 'Congaree National Park',
        'location': 'South Carolina',
        'activities': '',
        'campground': '',
        'video': ''
    },
    {
        'name': 'Wind Cave National Park',
        'location': 'South Dakota',
        'activities': '',
        'campground': '',
        'video': ''
    },
    {
        'name': 'Great Smoky Mountains National Park',
        'location': 'Tennessee',
        'activities': '',
        'campground': '',
        'video': ''
    },
    {
        'name': 'Big Bend National Park',
        'location': 'Texas',
        'activities': '',
        'campground': '',
        'video': ''
    },
    {
        'name': 'Great Smoky Mountains National Park',
        'location': 'Tennessee',
        'activities': '',
        'campground': '',
        'video': ''
    },
    {
        'name': 'Arches National Park',
        'location': 'Utah',
        'activities': '',
        'campground': '',
        'video': ''
    },
    {
        'name': 'Shenandoah National Park',
        'location': 'Virginia',
        'activities': '',
        'campground': '',
        'video': ''
    },
    {
        'name': 'Olympic National Park',
        'location': 'Washington',
        'activities': '',
        'campground': '',
        'video': ''
    },
    {
        'name': 'New River Gorge National Park',
        'location': 'West Virginia',
        'activities': '',
        'campground': '',
        'video': ''
    },
    {
        'name': 'Yellowstone National Park',
        'location': 'Wyoming',
        'activities': '',
        'campground': '',
        'video': ''
    },
    
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


    