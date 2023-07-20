import React, { useEffect, useState} from 'react'

function ActivitiesComponent() {
    const [activities, setActivities] = useState([])

    useEffect(()=>{
        fetchActivities();
    }, [])

    function fetchActivities(){
        fetch('/activities')
        .then(res => res.json())
        .then(data => setActivities(data))
    }


    return (
        <div>
            {activities.map(activity => (
                <div key={activity.id}> {activity.name}  </div>
            ))}
        </div>
      )
    }

    function CampgroundsComponent(){
        const [campgrounds, setCampgrounds] = useState([])

        useEffect(() => {
            fetch('/campgrounds')
              .then((res) => res.json())
              .then((data) => setCampgrounds(data));
          }, []);
    
    
        return(
            <div>
          <h2>Campgrounds</h2>
          {campgrounds.map((campground) => (
            <div key={campground.id}>{campground.name}</div>
          ))}
        </div>
        )

    }


    function VideosComponent() {
        const [videos, setVideos] = useState([]);
      
        useEffect(() => {
          fetch('/videos')
            .then((res) => res.json())
            .then((data) => setVideos(data));
        }, []);
      
        return (
          <div>
            <h2>Videos</h2>
            {videos.map((video) => (
              <div key={video.id}>{video.title}</div>
            ))}
          </div>
        );

    }

export {
    ActivitiesComponent,
    CampgroundsComponent,
    VideosComponent
}