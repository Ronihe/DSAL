function inflightEntertainment(movieLengths, flightLength) {
  const movieLengthsSeen = new Set();

  for (let i = 0; i < movieLengths.length; i++) {
    const movie1Length = movieLengths[i];
    // check the set is the set already has the movie
    const movie2Length = flightLength - movie1Length;

    // conditional statement
    if (movieLengthsSeen.has(movie2Length)) {
      return true;
    } else {
      movieLengthsSeen.add(movie1Length);
    }
  }
  console.log(false);
  return false;
}

inflightEntertainment([1, 2], 3);
