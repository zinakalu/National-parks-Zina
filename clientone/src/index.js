import React from 'react';
import ReactDOM from 'react-dom/client';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import App from './App';
import Search from './Search';
import ActivityFilter from './ActivityFilter';
import ParkDetails from './ParkDetails';
import { ActivitiesComponent, VideosComponent, CampgroundsComponent } from './ParkAttributes';
import { LoginComponent, SignupComponent, LogoutComponent } from './UserAuth';

const parks = {
  keyword: '',
  visited: [],
  park: {},
};

const setSearch = (keyword) => {
  parks.keyword = keyword;
};

const router = createBrowserRouter([
  { path: "/", element: <App />, children: [
    { path: '/Search', element: <Search setSearch={setSearch} parks={parks} /> },
    { path: '/activityFilter', element: <ActivityFilter parks={parks} /> },
    { path: '/park/:stateName', element: <ParkDetails parks={parks} /> },
    { path: '/activities', element: <ActivitiesComponent /> },
    { path: '/campgrounds', element: <CampgroundsComponent/> },
    { path: '/videos', element: <VideosComponent/> },
    { path: '/login', element:<LoginComponent /> },
    { path: '/signup', element:<SignupComponent /> },
    { path: '/logout', element:<LogoutComponent /> }
  ] },
]);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <RouterProvider router={router} />
);
