// 1. Define getBusinesses here:
//      Sample endpoint:
//      https://www.apitutor.org/yelp/simple/v3/businesses/search?q=tacos&location=Asheville+NC&limit=6
//      {rootURL}?q=${search_term}&location=${location}&limit=${num_results}


async function getBusinesses(search_term, location, num_results) {
    const endpoint = "https://www.apitutor.org/yelp/simple/v3/businesses/search";
    const url = `${endpoint}?location=${location}&q=${search_term}&limit=${num_results}`;
    const response = await fetch(url);
    const jsonData = await response.json();
    console.log(`Matches for ${search_term}:`, jsonData);
};



/****************/
/* Testing Code */
/****************/
// uncomment these lines of code when you've finished with Q1, and
// preview index.html in the browser using Live Server.

console.log('Should display 3 pizza restaurants in Asheville:', await getBusinesses('Asheville, NC', 'pizza', 3));
console.log('Should display 10 thai restaurants in San Francisco:', await getBusinesses('San Francisco, CS', 'thai', 10));
