from flask import Flask
from database import db
from models import User, Park
from faker import Faker
from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///national-parks.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
db.init_app(app)

fake = Faker()

parks = [
    {
        'name': 'Little River Canyon National Preserve',
        'location': 'Alabama',
        'activities': 'Hiking, Biking, Wildlife Viewing',
        'campground': 'Little River Canyon Campground',
        'video': 'https://www.youtube.com/watch?v=Lf631-M4RsA&ab_channel=WVTM13News'
    },
    {
        'name': 'Denali National Park',
        'location': 'Alaska',
        'activities': 'Climbing, Hiking, Wildlife Tours',
        'campground': 'DeSoto State Park, Little River RV Park & Campground',
        'video': 'https://www.youtube.com/watch?v=jFBot9rkCZs&ab_channel=RockThePark'
    },
    {
        'name': 'Grand Canyon National Park',
        'location': 'Arizona',
        'activities': 'Hiking, Rafting, Helicopter Tours',
        'campground': 'Mather Campground, Desert View Campground, North Rim Campground',
        'video': 'https://www.youtube.com/watch?v=dGGWu_noS3w&ab_channel=NationalGeographic'
    },
    {
        'name': 'Trail of Tears National Historic Trail',
        'location': 'Arkansas',
        'activities': 'Hiking, Historical Tours',
        'campground': 'Fort Smith National Historic Site',
        'video': 'https://www.youtube.com/watch?v=SosZ2ZRJymU&ab_channel=SmithsonianChannel'
    },
    {
        'name': 'Redwood National and State Parks',
        'location': 'California',
        'activities': 'Hiking, Wildlife Viewing, Biking',
        'campground': 'Jedediah Smith Campground, Mill Creek Campground',
        'video': 'https://www.youtube.com/watch?v=Hfx2s19QBRo&ab_channel=CreativeTravelGuide'
    },
    {
        'name': 'Great Sand Dunes National Park & Preserve',
        'location': 'Colorado',
        'activities': 'Sandboarding, Hiking, Wildlife Viewing',
        'campground': 'Pinon Flats Campground',
        'video': 'https://www.youtube.com/watch?v=HPb2IwY9Anw&ab_channel=GoTraveler'
    },
    {
        'name': 'Twin Brooks Park',
        'location': 'Connecticut',
        'activities': 'Picnicking, Playing Sports, Walking',
        'campground': 'N/A',
        'video': 'https://www.youtube.com/watch?v=Bdb0wOWg6pg&ab_channel=EdneiFerreira'
    },
    {
        'name': 'Chesapeake Bay Gateways and Watertrails',
        'location': 'Delaware',
        'activities': 'Boating, Fishing, Wildlife Viewing',
        'campground': 'Cape Henlopen State Park',
        'video': 'https://www.youtube.com/watch?v=DSOIu0LCOG0&ab_channel=SchoandJo'
    },
    {
        'name': 'Dry Tortugas National Park',
        'location': 'Florida',
        'activities': 'Snorkeling, Camping, Wildlife Viewing',
        'campground': 'Garden Key Campground',
        'video': 'https://www.youtube.com/watch?v=F6o2EZPNSRA&ab_channel=VISITFLORIDA'
    },
    {
        'name': 'Chattahoochee River National Recreation Area',
        'location': 'Georgia',
        'activities': 'Fishing, Hiking, Paddling',
        'campground': 'Sweetwater Creek State Park',
        'video': 'https://www.youtube.com/watch?v=BAOAXbZHcAo&ab_channel=MetroOnTheMove'
    },
    {
        'name': 'Kalaupapa National Historic Park',
        'location': 'Hawaii',
        'activities': 'Historical Tours, Hiking, Wildlife Viewing',
        'campground': 'N/A',
        'video': 'https://www.youtube.com/watch?v=50e1FmMRVgY&ab_channel=TheHIEscapade'
    },
    {
        'name': 'Yellowstone National Park',
        'location': 'Idaho',
        'activities': 'Wildlife Viewing, Hiking, Backpacking, Fishing',
        'campground': 'Mammoth Campground, Grant Village Campground',
        'video': 'https://www.youtube.com/watch?v=YjPGz9192S0&ab_channel=WorldWildHearts'
    },
    {
        'name': 'Mammoth Cave National Park',
        'location': 'Kentucky',
        'activities': 'Cave Tours, Canoeing and Kayaking, Hiking, Wildlife Viewing ',
        'campground': 'Mammoth Cave Campground, Maple Springs Group Campground',
        'video': 'https://www.youtube.com/watch?v=fTNlZl7-s4w&ab_channel=GoTraveler'
    },
    {
        'name': 'Indiana Dunes National Park',
        'location': 'Indiana',
        'activities': 'swimming, hiking, birdwatching',
        'campground': 'Dunewood Campground, Indiana Dunes State Park',
        'video': 'https://www.youtube.com/watch?v=qat0Pakzur4&ab_channel=ThroughMyLens'
    },
    {
        'name': 'Acadia National Park',
        'location': 'Maine',
        'activities': 'hiking, biking, rock climbing, wildlife watching',
        'campground': 'Blackwoods Campground, Seawall Campground',
        'video': 'https://www.youtube.com/watch?v=mCzNCvompGI&ab_channel=ViewCation'
    },
    {
        'name': 'Isle Royale National Park',
        'location': 'Michigan',
        'activities': 'hiking, backpacking, Kayaking and Canoeing, fishing, wildlife watching',
        'campground': 'Rock Harbor Campground, Daisy Farm Campground',
        'video': 'https://www.youtube.com/watch?v=4cxWWTSHui4&ab_channel=PureMichigan'
    },
    {
        'name': 'Voyageurs National Park',
        'location': 'Minnesota',
        'activities': 'Boating and Canoeing, fishing, hiking, wildlife viewing',
        'campground': 'Rainy Lake Visitor Center Campground, Kabetogama Lake Visitor Center Campground',
        'video': 'https://www.youtube.com/watch?v=Uj5GosWchzU&ab_channel=JourneytoAllNationalParks'
    },
    {
        'name': 'Gateway Arch National Park',
        'location': 'Missouri',
        'activities': 'picnicking',
        'campground': 'St. Louis RV Park, Sundermeier RV Park',
        'video': 'https://www.youtube.com/watch?v=vypL3nh3_m8&ab_channel=ThroughMyLens'
    },
    {
        'name': 'YellowStone National Park',
        'location': 'Montana',
        'activities': 'Wildlife Viewing, Hiking, Backpacking, Fishing',
        'campground': 'Mammoth Campground, Grant Village Campground',
        'video': 'https://www.youtube.com/watch?v=YjPGz9192S0&ab_channel=WorldWildHearts'
    },
    {
        'name': 'Death Valley National Park',
        'location': 'Nevada',
        'activities': 'Stargazing, hiking, Badwater Basin',
        'campground': 'Furnace Creek Campground, Mesquite Spring Campground',
        'video': 'https://www.youtube.com/watch?v=Lh19rOVB0kY&ab_channel=Expedia'
    },
    {
        'name': 'White Sands National Park',
        'location': 'New Mexico',
        'activities': 'Sand Sledding, Sandboarding, Scenic Drives, hiking',
        'campground': 'Oliver Lee Memorial State Park, Alamogordo/White Sands KOA',
        'video': 'https://www.youtube.com/watch?v=GhmRmhrs808&ab_channel=ThroughMyLens'
    },
    {
        'name': 'Theodore Roosevel National Park',
        'location': 'North Dakota',
        'activities': 'Scenic Drives, hiking, wildlife viewing, Horseback Riding, camping',
        'campground': 'Cottonwood Campground, Roundup Group Horse Campground',
        'video': 'https://www.youtube.com/watch?v=o7X2oPGLGq8&ab_channel=MoreThanJustParks'
    },
    {
        'name': 'Great Smoky Mountains National Park',
        'location': 'North Carolina',
        'activities': 'Scenic Drives, hiking, wildlife viewing,, fishing, wildlife viewing',
        'campground': 'Elkmont Campground, Cades Cove Campground, Smokemont Campground',
        'video': 'https://www.youtube.com/watch?v=poyWuEA6HT0&ab_channel=NationalGeographic'
    },
    {
        'name': 'Cuyahoga Valley National Park',
        'location': 'Ohio',
        'activities': 'hiking, biking, kayaking, canoeing, fishing',
        'campground': 'Stanford House, Backpacking',
        'video': 'https://www.youtube.com/watch?v=eZvmw3_u9H8&ab_channel=21stCenturyPioneer'
    },
    {
        'name': 'Crater Lake National Park',
        'location': 'Oregon',
        'activities': 'hking, boat tours, cross-country skiing',
        'campground': 'Mazama Campground, Lost Creek Campground',
        'video': 'https://www.youtube.com/watch?v=Pcn8nivQYyY&ab_channel=ShoreMeSomeMore'
    },
    {
        'name': 'Congaree National Park',
        'location': 'South Carolina',
        'activities': 'hiking, Canoeing, Kayaking, Birdwatching',
        'campground': 'N/A',
        'video': 'https://www.youtube.com/watch?v=SzDp5HHHp_M&ab_channel=DQFamilyTravel'
    },
    {
        'name': 'Wind Cave National Park',
        'location': 'South Dakota',
        'activities': 'cave tours, hiking, Scenic Drives, wildlife viewing',
        'campground': 'Elk Mountain Campground, Custer State Park',
        'video': 'https://www.youtube.com/watch?v=SkAxHMB1g6Y&ab_channel=GoTraveler'
    },
    {
        'name': 'Great Smoky Mountains National Park',
        'location': 'Tennessee',
        'activities': 'Scenic Drives, hiking, wildlife viewing,, fishing, wildlife viewing',
        'campground': 'Elkmont Campground, Cades Cove Campground, Smokemont Campground',
        'video': 'https://www.youtube.com/watch?v=poyWuEA6HT0&ab_channel=NationalGeographic'
    },
    {
        'name': 'Big Bend National Park',
        'location': 'Texas',
        'activities': 'River Rafting, Kayaking, Scenic Drives, hiking, wildlife viewing',
        'campground': 'Chisos Basin Campground, Cottonwood Campground',
        'video': 'https://www.youtube.com/watch?v=D8X5w24VD1M&ab_channel=GoTraveler'
    },
    {
        'name': 'Arches National Park',
        'location': 'Utah',
        'activities': 'Scenic Drives, hiking, rock climbing',
        'campground': 'Devils Garden Campground',
        'video': 'https://www.youtube.com/watch?v=WwtRH6mgHks&ab_channel=Expedia'
    },
    {
        'name': 'Shenandoah National Park',
        'location': 'Virginia',
        'activities': 'Scenic Drives, hiking, wildlife viewing',
        'campground': 'Big Meadows Campground, Loft Mountain Campground:',
        'video': 'https://www.youtube.com/watch?v=0GSUBRrrwNs&ab_channel=ShoreMeSomeMore'
    },
    {
        'name': 'Olympic National Park',
        'location': 'Washington',
        'activities': '',
        'campground': 'Sol Duc Hot Springs Resort Campground, Kalaloch Campground, Mora Campground',
        'video': 'https://www.youtube.com/watch?v=NEMQdNYbBds&ab_channel=NationalGeographic'
    },
    {
        'name': 'New River Gorge National Park',
        'location': 'West Virginia',
        'activities': 'Whitewater Rafting, Kayaking, Mountain Biking, hiking, Scenic Drives',
        'campground': 'Canyon Rim Campground, Army Camp Campground',
        'video': 'https://www.youtube.com/watch?v=__lLTJmTsp4&ab_channel=MoreThanJustParks'
    },
    {
        'name': 'Yellowstone National Park',
        'location': 'Wyoming',
        'activities': 'Wildlife Viewing, Hiking, Backpacking, Fishing',
        'campground': 'Mammoth Campground, Grant Village Campground',
        'video': 'https://www.youtube.com/watch?v=YjPGz9192S0&ab_channel=WorldWildHearts'
    },
    
]

def clear_previous_seeds():
    with app.app_context():
        db.drop_all()
        db.create_all()

def seed_data():
    clear_previous_seeds()
    
    with app.app_context():
        for _ in range(60):
            user = User(username=fake.user_name(), _password_hash=fake.password(), image_url=fake.url())
            db.session.add(user)
        db.session.commit()

        for park_info in parks:
            park = Park(name=park_info.get('name'),
                        location=park_info.get('location'),
                        activities=park_info.get('activities'),
                        campgrounds=park_info.get('campground'),
                        videos=park_info.get('video'),
                        user_id = User.query.order_by(func.random()).first().id)

            db.session.add(park)
        db.session.commit()

if __name__ == '__main__':
    seed_data()