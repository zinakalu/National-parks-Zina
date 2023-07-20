import React, { useState } from "react";

function ActivityFilter({ activities }) {
  const [filter, setFilter] = useState('');
  const [categories, setCategories] = useState(['hiking', 'biking', 'wildlife viewing', 'climbing', 'wildlife tours', 'rafting', 'helicopter tours', 'historical tours', 'sandboarding', 'picknicking']);

  const handleFilter = (e) => {
    setFilter(e.target.value);
  };

  const handleCategoryChange = (e) => {
    setCategories(e.target.value);
  };

  const filteredActivities = activities.filter((activity) => {
    return activity.keyword.toLowerCase().includes(filter.toLowerCase()) && categories.includes(activity.category);
  });

  if (filteredActivities.length === 0) {
    console.log('No matching activities found.');
  } else {
    console.log('Matching activities:', filteredActivities);
  }

  return (
    <div>
      <input
        type="text"
        placeholder="Filter by keyword..."
        value={filter}
        onChange={handleFilter}
      />
      <select value={categories} onChange={handleCategoryChange}>
        <option value="">All Categories</option>
        {categories.map((category) => (
          <option key={category} value={category}>{category}</option>
        ))}
      </select>
      <ul>
        {filteredActivities.map((activity) => (
          <li key={activity.keyword}>{activity.keyword}</li>
        ))}
      </ul>
    </div>
  );
}

export default ActivityFilter;