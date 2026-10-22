Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Los Angeles Community College District: The Los Angeles Community College District (LACCD) is the community college district serving Los Angeles, California, United States and some of its neighboring cities and certain unincorporated areas of Los Angeles County.  Its headquarters are in Downtown Los Angeles.  Over the past seventy-seven years LACCD has served as educator to more than three million students.  In addition to typical college aged students, the LACCD also serves adults of all ages.  Indeed, over half of all LACCD students are older than 25 years of age, and more than a quarter are 35 or older.  LACCD educates almost three times as many Latino students and nearly four times as many African-American students as all of the University of California campuses combined.  Eighty percent of LACCD students are from underserved populations.  The Los Angeles Community College District is the largest community college district in the United States and is one of the largest in the world.  The nine colleges within the district offer educational opportunities to students in Los Angeles.  It serves students located in the Alhambra, Beverly Hills, Burbank, Culver City, Garvey, Las Virgenes, Los Angeles, Montebello, Palos Verdes and San Gabriel school districts.  The district covers the Los Angeles city limits, San Fernando, Calabasas, Agoura Hills, Hidden Hills, Burbank, West Hollywood, Beverly Hills, Culver City, Alhambra, Monterey Park, San Gabriel, Rosemead (southern portion), Montebello, Commerce, Vernon, Huntington Park, Bell, Cudahy, Bell Gardens, South Gate, Gardena, Carson, Lomita, Palos Verdes Estates, Rolling Hills, Rancho Palos Verdes, and numerous unincorporated communities, including East Los Angeles, Florence-Firestone, Athens, and Walnut Park.  The LACCD consists of nine colleges and covers an area of more than 882 sqmi .

Culver CityBus: Culver CityBus is a public transport agency operating in Culver City, California, currently serving Culver City, the unincorporated community of Marina del Rey, and the adjacent Los Angeles neighborhoods.  Its regular fleet is painted bright green and its rapid fleet primarily a chrome gray, distinguishing it from Santa Monica's Big Blue Bus, orange-colored Metro Local buses, and red-colored Metro Rapid buses, whose coverage areas overlap on Los Angeles's Westside.

Carlson Park, Culver City, California: Carlson Park is a suburban neighborhood in central Culver City, California.  It is named for Dr. Paul Carlson Park, a city park in the center of the neighborhood, which is named for Culver City native Dr. Paul Carlson, a medical missionary martyred in the former Belgian Congo.  Students residing in the neighborhood are zoned either to Linwood E. Howe Elementary or Farragut Elementary, and to Culver City Middle School and Culver City High School.  Its ZIP code is 90232.

Doris Bither case: The Doris Bither case, also known as the Entity hauntings, was an alleged haunting which occurred in 1974 at Culver City, California where a woman named Doris Bither alleged the ghosts of three Asian men were raping her.  The case inspired Frank De Felitta's 1978 book "The Entity" which was made into a 1982 film of the same name starring Barbara Hershey.

Culver Hotel: The Culver Hotel is a national historical landmark in downtown Culver City, California.  It was built by Harry Culver, the founder of Culver City, and opened on September 4, 1924, with local headlines announcing: "City packed with visitors for opening of Culver skyscraper."  Originally named Hotel Hunt, and later known as Culver City Hotel, the six-story Renaissance Revival building was designed by Curlett & Beelman, the architecture firm behind renowned Art Deco buildings throughout Los Angeles, including downtown Los Angeles' Roosevelt and Eastern Columbia buildings.

Culver City Stairs: The Baldwin Hills Scenic Overlook California State Park is located just southwest of downtown Culver City.  To some Los Angeles area residents, the site is more commonly known as the Culver City Stairs.  This outdoor staircase is designed into the trails leading up to a view of the greater Los Angeles area.  The street address for the park is 6300 Hetzler Road, Culver City, California 90232.

Wende Museum: The Wende Museum of the Cold War is an art museum, historical archive, and educational institution in Culver City, California.  It was founded in 2002 by Justinian Jampol and has a collection of more than 100,000 unique objects of visual and material culture from the Soviet Union and the former Eastern Bloc.  In November 2012, the City Council of Culver City voted unanimously to approve a 75-year lease of the former United States National Guard Armory building in Culver City as the permanent location of the Wende Museum.  The Armory building was constructed by the National Guard in 1949, when the Cold War began to escalate, and was decommissioned in March 2011.  The museum is expected to open at the Armory site in late 2016 following renovations.

CulverLand: CulverLand is a temporary artwork and functioning game in Culver City, California, United States, created by John Derevlany.  It was funded by an arts grant from the City of Culver City, California, and installed as part of the 2010 Indiecade, the International Festival of Independent Games.

The Entity: The Entity is a 1982 American horror film directed by Sidney J. Furie and written by Frank De Felitta, who adapted his 1978 novel of the same name.  It stars Barbara Hershey as a woman who is raped and tormented by an invisible assailant.  Despite being filmed and planned for a release in 1981, the movie was not released in worldwide theaters until September 1982 and February 1983 in the United States.  Like the novel, the film is based on the 1974 Doris Bither case.

Culver City High School: Culver City High School is the main public high school of the Culver City Unified School District (CCUSD) in Culver City, California.  It was opened in 1951.  The school's colors are blue and silver, and the mascot is the centaur.  As of 2014, its enrollment was roughly 2,000.  Culver City High School is recognized as a California Distinguished School, earning the honor in 2005.

Question: What case from Culver City, California had a horror film from 1982 based upon it?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "case_name": {
      "type": "string",
      "description": "The name of the case."
    },
    "case_location": {
      "type": "string",
      "description": "The city and state where the case occurred."
    },
    "case_year": {
      "type": "integer",
      "description": "The year the case occurred."
    },
    "inspired_film": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film inspired by the case."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the film."
        },
        "genre": {
          "type": "string",
          "description": "The genre of the film."
        },
        "main_actor": {
          "type": "string",
          "description": "The name of the main actor in the film."
        }
      },
      "required": [
        "title",
        "release_year",
        "genre",
        "main_actor"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "case_name",
    "case_location",
    "case_year",
    "inspired_film"
  ],
  "additionalProperties": false
}
