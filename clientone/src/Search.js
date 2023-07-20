import React from 'react';

function Search({ setSearch, parks }) {
  const [search, setSearchState] = React.useState('');

  function handleChange(event) {
    setSearchState(event.target.value);
  }

  const filteredParks = parks.filter((park) => {
    return park.park.toLowerCase().includes(search.toLowerCase());
  });

  return (
    <div>
      <input
        type="text"
        placeholder="Search for a park..."
        value={search}
        onChange={handleChange}
      />
      <ul>
        {filteredParks.map((park) => (
          <li key={park.park}>{park.park}</li>
        ))}
      </ul>
    </div>
  );
}

export default Search