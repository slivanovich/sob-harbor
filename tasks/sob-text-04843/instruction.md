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
Space Mountain (Magic Kingdom): Space Mountain is an indoor dark outer space-themed steel roller coaster at the Magic Kingdom theme park at the Walt Disney World Resort in Lake Buena Vista, Florida.  Opened on January 15, 1975, Space Mountain is the oldest operating roller coaster in the state of Florida, and is the original version of the iconic attraction that has since been replicated at all of The Walt Disney Company's Magic Kingdom-style theme parks worldwide, except for the Shanghai Disneyland Resort.  RCA helped fund Space Mountain's construction and sponsored the ride from 1975 to 1993; FedEx sponsored Space Mountain from 1994 to 2004.

Hilton Orlando Lake Buena Vista: The Hilton Orlando Lake Buena Vista is an AAA Four-Diamond hotel located adjacent to the Disney Springs complex located on Walt Disney World Resort property in Lake Buena Vista, Florida.  The 23 acre hotel, which opened in November 1983, is among seven hotels that make up the Disney Springs Resort Area.  The Disney Springs Resort Area Hotels are located on the property of the Walt Disney World Resort in Lake Buena Vista, Florida, but are not operated by Disney.

Toy Story Midway Mania!: Toy Story Midway Mania!  (marketed as Toy Story Mania!)  is an interactive 4-D theme park attraction, located at three Disney theme parks: Disney's Hollywood Studios at the Walt Disney World Resort in Florida, Disney California Adventure at the Disneyland Resort and Tokyo DisneySea at Tokyo Disney Resort.

Best Western Lake Buena Vista Resort Hotel: The Best Western Lake Buena Vista Resort Hotel is a 325-room resort that is on the property of Walt Disney World Resort in Lake Buena Vista, Florida.  The resort is located across from the Disney Springs area.  The hotel originally opened in November 1972 as the Travelodge at Lake Buena Vista.  It was operated by Travelodge from 1972 through 1983, then in 1984 the resort became the Viscount Hotel and operated as such until 1988.  In 1989, it was reacquired by Travelodge.  In 2000, the Travelodge hotel switched over to become the Best Western Lake Buena Vista Resort Hotel.  The hotel was renovated in 2004 and has 2 outdoor pools.

Tower of Terror (film): Tower of Terror is a 1997 made-for-TV supernatural thriller directed by D. J. MacHale.  It is based on the theme park attraction, The Twilight Zone Tower of Terror, at Disney's Hollywood Studios at the Walt Disney World Resort in Bay Lake, Florida and was originally a presentation of "The Wonderful World of Disney".  It is also Disney's first film based on an attraction at one of its theme parks, and the only adaptation to be made for television.

The Lottery (1989 film): The Lottery is a 1989 American short film starring Bette Midler and directed by Garry Marshall which was shown at the then Disney-MGM Studios in line for the first versions of the Studio Backlot Tour.

Who Wants to Be a Millionaire – Play It!: Who Wants To Be A Millionaire - Play It!  was an attraction at Disney's Hollywood Studios (formerly "Disney-MGM Studios") theme park at Walt Disney World Resort in Orlando, Florida and Disney California Adventure in Anaheim, California.  The attraction was a modified version of the "Who Wants to Be a Millionaire" television game show.

Moteurs... Action! Stunt Show Spectacular: The Moteurs... Action!  Stunt Show Spectacular or Lights, Motors, Action!  Extreme Stunt Show is a stunt show performed at Walt Disney Studios Park in Disneyland Paris and formerly performed at Disney's Hollywood Studios theme park in Lake Buena Vista, Florida.  The "Moteurs... Action!"  show originally premiered with the Walt Disney Studios Park when it opened in March 2002.  The "Lights, Motors, Action!"  version of the show debuted three years later at Disney's Hollywood Studios as part of the Happiest Celebration on Earth festival, in which each of the four Walt Disney World theme parks opened a new attraction that been copied from another Disney resort.

Studio Backlot Tour: The Studio Backlot Tour was a theme park attraction at Disney's Hollywood Studios theme park at the Walt Disney World Resort in Lake Buena Vista, Florida.  It was a combination of a walking and tram tour of the backlot area of the park.  The Studio Backlot Tour was one of two original attractions at Disney's Hollywood Studios, the other being the Great Movie Ride.

Disney's Hollywood Studios: Disney's Hollywood Studios is a theme park at the Walt Disney World Resort in Bay Lake, Florida, near Orlando.  It is owned and operated by The Walt Disney Company through its Parks and Resorts division.  Based on an idea by Marty Sklar, Randy Bright, and Michael Eisner, the park opened on May 1, 1989, as the Disney-MGM Studios Theme Park, and was the third of four theme parks built at Walt Disney World.  Spanning 135 acres , the park is dedicated to the facets of show business, including film, television, music, and theatre, drawing inspiration from the heyday of Hollywood in the 1930s and 1940s.

Question: The Lottery is a 1989 American short film starring Bette Midler, which was shown at the then Disney-MGM Studios in line for the first versions of the Studio Backlot Tour was a theme park attraction at Disney's Hollywood Studios theme park at the Walt Disney World Resort in Lake Buena Vista, in which state? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string"
        },
        "year": {
          "type": "integer"
        }
      },
      "required": [
        "title",
        "year"
      ],
      "additionalProperties": false
    },
    "attraction_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    },
    "theme_park_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "resort_name": {
          "type": "string"
        }
      },
      "required": [
        "name",
        "resort_name"
      ],
      "additionalProperties": false
    },
    "location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string"
        },
        "state": {
          "type": "string"
        }
      },
      "required": [
        "city",
        "state"
      ],
      "additionalProperties": false
    },
    "answer_state": {
      "type": "string"
    }
  },
  "required": [
    "film_details",
    "attraction_details",
    "theme_park_details",
    "location",
    "answer_state"
  ],
  "additionalProperties": false
}
