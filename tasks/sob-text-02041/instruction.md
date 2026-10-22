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
Celebrate Israel Parade: Celebrate Israel Parade (originally Youth Salute to Israel Parade then Salute to Israel Parade) is an annual parade in support of Israel that takes place along Fifth Avenue in New York.  The parade travels north on Fifth Avenue from 57th Street to 74th Street.

Lynching of Jesse Washington: Jesse Washington was a black teenage farmhand who was lynched in Waco, Texas, on May 15, 1916, in what became a well-known example of racially motivated lynching.  Washington was convicted of raping and murdering Lucy Fryer, the wife of his white employer in rural Robinson, Texas.  He was dragged out of the court by observers and lynched in front of Waco's city hall.  Over 10,000 spectators, including city officials and police, gathered to watch the attack.  There was a celebratory atmosphere at the event, and many children attended during their lunch hour.  Members of the mob castrated Washington, cut off his fingers, and hung him over a bonfire.  He was repeatedly lowered and raised over the fire for about two hours.  After the fire was extinguished, his charred torso was dragged through the town and parts of his body were sold as souvenirs.  A professional photographer took pictures as the event unfolded, providing rare imagery of a lynching in progress.  The pictures were printed and sold as postcards in Waco.

252 East 57th Street: 252 East 57th Street is a mixed use modernist style residential skyscraper in New York City, United States developed by the World Wide Group and Rose Associates, Inc.  Construction started in 2013, 252 East 57th Street is part of a surge of redevelopment of 57th Street into a luxury residential corridor that has been named "Billionaires’ Row."  The residential tower will be 712 feet tall with condominiums starting on the 36th floor.  The building will also include the construction of two new schools and 78,000 square feet of retail space, in addition to a Whole Foods Market.  The residential tower and additional retail portions are anticipated to open in late 2016.

Silent Parade: The Negro Silent Protest Parade was a silent march of about 10,000 African Americans along Fifth Avenue starting at 57th Street in New York City on July 28, 1917.  The event was organized by the NAACP, church, and community leaders to protest violence directed towards African Americans, such as recent lynchings in Waco and Memphis.  The parade was precipitated by the East St. Louis riots in May and July 1917 where at least 40 black people were killed by white mobs, in part touched off by a labor dispute where blacks were used for strike breaking.

Fifth Avenue Transportation Company: The Fifth Avenue Transportation Company was a transportation company based in New York which was founded in 1885 and operated of horse-and-omninbus transit along Fifth Avenue, with a route running from 89th Street to Bleecker Street using horse-drawn omnibuses.  Fifth Avenue was unusual in that its residents opposed the installation of railway track for streetcars and was the only avenue in Manhattan to never see streetcar service.  The company was declared bankrupt of the earlier operator in 1896, and was succeeded by the Fifth Avenue Coach Company

L.P. Hollander Company Building: The L.P. Hollander Company Building is located at 3 East 57th Street, New York City.  The edifice received the 1930 gold medal of the Fifth Avenue Association for the "best structure" built in the Fifth Avenue district during the year.  The L.P. Hollander Company Building was erected prior to the Empire State Building and 500 Fifth Avenue, which were judged for the year 1931.  The Empire State Building and the Lilly Dache Building were designed by William F. Lamb of Shreve, Lamb & Harmon, architects, who was responsible for planning the L.P. Hollander Building.  The Hollander Building was built by Starrett Brothers & Eken.

36th Street (BMT Fifth Avenue Line): 36th Street was a station on the demolished section of the BMT Fifth Avenue Line.  It was served by trains of the BMT Culver Line and BMT Fifth Avenue Line.  It had four tracks and two island platforms.  The station was opened on May 29, 1890, and was the southern terminus of the Fifth Avenue Line until 1893, as well as the southernmost station to be installed along Fifth Avenue itself.  Stations built beyond this point were located along Third Avenue, and the line was sometimes called the BMT Third Avenue Line south of here.  The next stop to the north was 25th Street.  The next stop to the south was Ninth Avenue for Culver Line trains and 40th Street for Fifth Avenue Line trains.  Ninth Avenue station still exists today exclusively for the BMT West End Line.  The station closed on May 31, 1940.  Current rapid transit service in this area can be found one block west at the 36th Street Station on the underground BMT Fourth Avenue Line.

40th Street (BMT Fifth Avenue Line): 40th Street was a station on the now demolished BMT Fifth Avenue Line.  It was served by trains of the BMT Fifth Avenue Line.  It had two tracks and one island platform.  The station was built on October 1, 1893, and despite the name of the line was actually located on Third Avenue and 40th Street.  It was the northernmost station on Third Street before the line shifted to the street that bore its name.  The station had connections to four streetcar lines; The Church Avenue Line, 39th Street and Coney Island Line, 39th Street and Manhattan Beach Line, and 39th Street and Ulmer Park Line.  The next stop to the north was 36th Street.  The next stop to the south was 46th Street.  The station closed on May 31, 1940.

25th Street (BMT Fifth Avenue Line): 25th Street was a station on the now demolished BMT Fifth Avenue Line in New York.  It was served by trains of the BMT Culver Line and BMT Fifth Avenue Line.  It had two tracks and one island platform.  The station was opened on August 15, 1889, at Fifth Avenue and 25th Street, and was the southern terminus of the line until 1890.  The next stop to the north was 20th Street.  The next stop to the south was 36th Street.  The station closed on May 31, 1940.  Current rapid transit service in this area can be found one block west at the 25th Street Station on the underground BMT Fourth Avenue Line.

16th Street (BMT Fifth Avenue Line): 16th Street was a station on the demolished section of the BMT Fifth Avenue Line.  It was served by trains of the BMT Culver Line and BMT Fifth Avenue Line and had 2 tracks and 1 island platform.  The station was built on August 15, 1889, at the intersection of Fifth Avenue and 16th Street, and had a connection to the 15th Street Line trolleys.  The next stop to the north was Ninth Street.  The next stop to the south was 20th Street.  It closed on May 31, 1940.

Question: In which state was the black farmhand lynched in 1916 in with over 10,000 spectators, that prompted Silent Parade with about 10,000 African Americans along Fifth Avenue starting at 57th Street in New York City the next year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "lynching_event": {
      "type": "object",
      "properties": {
        "victim_name": {
          "type": "string",
          "description": "Name of the person lynched."
        },
        "year": {
          "type": "integer",
          "description": "Year the lynching occurred."
        },
        "location": {
          "type": "object",
          "properties": {
            "city": {
              "type": "string",
              "description": "City where the lynching took place."
            },
            "state": {
              "type": "string",
              "description": "State where the lynching took place."
            }
          },
          "required": [
            "city",
            "state"
          ],
          "additionalProperties": false
        },
        "spectator_count": {
          "type": "integer",
          "description": "Number of spectators at the lynching event."
        }
      },
      "required": [
        "victim_name",
        "year",
        "location",
        "spectator_count"
      ],
      "additionalProperties": false
    },
    "prompting_event": {
      "type": "object",
      "properties": {
        "event_name": {
          "type": "string",
          "description": "Name of the event prompted by the lynching."
        },
        "year": {
          "type": "integer",
          "description": "Year the prompted event occurred."
        },
        "participant_count": {
          "type": "integer",
          "description": "Number of participants in the prompted event."
        },
        "location_details": {
          "type": "object",
          "properties": {
            "street": {
              "type": "string",
              "description": "Street where the prompted event started."
            },
            "start_street_number": {
              "type": "integer",
              "description": "Starting street number for the prompted event."
            },
            "city": {
              "type": "string",
              "description": "City where the prompted event took place."
            }
          },
          "required": [
            "street",
            "start_street_number",
            "city"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "event_name",
        "year",
        "participant_count",
        "location_details"
      ],
      "additionalProperties": false
    },
    "final_answer_state": {
      "type": "string",
      "description": "The state where the black farmhand was lynched."
    }
  },
  "required": [
    "lynching_event",
    "prompting_event",
    "final_answer_state"
  ],
  "additionalProperties": false
}
