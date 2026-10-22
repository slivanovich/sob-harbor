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
John Henry Moss Stadium: John Henry Moss Stadium is a baseball stadium home to the Gardner-Webb University Runnin' Bulldogs.  It was officially completed on September 18, 2010.  The first regular season game played there was February 22, 2011.  It has a capacity of about 700, but can be expanded.  John Henry Moss was born in Kings Mountain, North Carolina, and was president of the South Atlantic League for 50 years.  He was the youngest person to be a president of a professional baseball league, taking over the Western Carolina League in 1948 at the age of 29.

Oestrike Stadium: Oestrike Stadium is a stadium in Ypsilanti, Michigan at Eastern Michigan University.  It is named after Ron Oestrike, a former baseball coach at EMU.  It is primarily used for baseball, and serves as the Eastern Michigan University Eagles baseball team home field.  In addition, it served as the home field of the Midwest Sliders of Ypsilanti Frontier League baseball team in 2009 and 2010 (the Sliders were renamed the Oakland County Cruisers their second season at Oestrike Stadium as a result of their planned move to Waterford Township).  Several present and former major leaguers, including Bob Welch, Bob Owchinko, Bryan Clutterbuck, Pat Sheridan, and Brian Bixler, played at Oestrike Stadium as members of the EMU baseball team.

Kokomo Municipal Stadium: Kokomo Municipal Stadium is a baseball stadium in Kokomo, Indiana, United States.  The Kokomo Jackrabbits of the college summer Prospect League, and the Kokomo Wildkats (local high school) plan to use Kokomo Municipal Stadium as their home field.  Other local high school baseball teams including the Taylor Titans, Northwestern Tigers, and the Western Panthers plan to use the Kokomo Municipal Stadium for a portion of their games.  Upon opening in 2015, Kokomo Municipal Stadium will have a capacity of up to 4,000 in a combination of fixed and lawn seating.  In May 2016, the Kokomo Mantis FC of the Premier Development League will call the stadium home.

Kelowna Falcons: The Kelowna Falcons are an amateur baseball team located in Kelowna, British Columbia.  Formally known as the Kelowna Grizzlies, the club was purchased in 2000 and changed its name to the Falcons.  They play in the West Coast League, a collegiate summer baseball league.  Kelowna calls Elks Stadium home with the capacity of 1250.

Centene Stadium: Centene Stadium is a stadium in Great Falls, Montana.  It is named for the Centene Corporation which paid for the naming rights to the stadium.  It is primarily used for baseball, and is the home field of the Great Falls Voyagers minor league baseball team.  It was built in 1940 and holds 4,000 people.  The ballpark has a picnic area and a BBQ area.  Field dimensions are 335 to right field, 328 to left field, 415 to center field, and 368 to each power alley.

Moana Stadium: Moana Stadium was a stadium in Reno, Nevada.  It was primarily used for baseball.  Teams that called the stadium home included the Reno Silver Sox, the Reno Blackjacks, Reno Padres and Reno Chukars.  The ballpark had a capacity of 4,000 people.  Moana Stadium was part of a city sports park.  The stadium was demolished in 2012 to make room for a new city pool and athletic fields on the site.

Great Falls Voyagers: The Great Falls Voyagers are a minor league baseball team based in Great Falls, Montana.  The team has played continuously in the Pioneer League since 1969, and previously played in the league from 1948 to 1963.  The Voyagers have been the Advanced Rookie affiliate of the Chicago White Sox since 2003.  Previously, the team was affiliated with the Los Angeles Dodgers (1984–2002), San Francisco Giants (1969–83), and Brooklyn/Los Angeles Dodgers (1952–63).  The team was not affiliated with any Major League Baseball team from 1964 to 1968.  The Voyagers play their home games at Centene Stadium.

Tulsa Roughnecks FC: The Tulsa Roughnecks FC is an American professional soccer team based in Tulsa, Oklahoma.  They compete in the United Soccer League, starting in the 2015 season.  Jeff and Dale Hubbard, co-owners of the Tulsa Drillers minor league baseball franchise, were announced as co-owners on December 18, 2013.  The team calls itself the Roughnecks after the name received nearly 50% of the votes in a "name the team" contest held in February 2014.

Appeal play: In baseball, an appeal play occurs when a member of the defensive team calls the attention of an umpire to an infraction which he would otherwise ignore.

Walla Walla Sweets: The Walla Walla Sweets is an amateur baseball team located in Walla Walla, Washington.  They play in the West Coast League, a collegiate summer baseball league.  Walla Walla calls Borleske Stadium home which has a capacity of 2,378 spectators.

Question: What baseball team calls Centene Stadium home?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "stadium_name": {
      "type": "string",
      "description": "The name of the stadium."
    },
    "home_team": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the baseball team that calls the stadium home."
        },
        "league_type": {
          "type": "string",
          "description": "The type of league the team belongs to (e.g., minor league, college, amateur)."
        }
      },
      "required": [
        "name",
        "league_type"
      ],
      "additionalProperties": false
    },
    "stadium_location": {
      "type": "string",
      "description": "The city and state where the stadium is located."
    },
    "stadium_capacity": {
      "type": "integer",
      "description": "The capacity of the stadium in number of people."
    }
  },
  "required": [
    "stadium_name",
    "home_team",
    "stadium_location",
    "stadium_capacity"
  ],
  "additionalProperties": false
}
