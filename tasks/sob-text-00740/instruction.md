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
Virtual Magic Kingdom: Virtual Magic Kingdom, also known as VMK, was a massively multiplayer online game developed by Walt Disney Parks and Resorts and Sulake Corporation and published by The Walt Disney Company.  It was a virtual representation of the Disneyland style theme parks, containing areas and minigames which were based on real park scenery and attractions.  It was launched as part of the Happiest Celebration on Earth promotional campaign to commemorate fifty years of Disney theme parks.

Delta Dreamflight: Delta Dreamflight was an attraction located in Tomorrowland at the Magic Kingdom inside the Walt Disney World Resort, and was sponsored by Delta Air Lines.  Dreamflight replaced an attraction called If You Could Fly, which was originally the attraction, If You Had Wings, sponsored by Eastern Air Lines.

Sesame Street 4-D Movie Magic: Sesame Street 4-D Movie Magic (titled Sesame Street Presents Lights Camera Imagination!  4-D at SeaWorld and Busch Gardens Europe parks, and Sesame Street Film Festival 4-D at Busch Gardens Africa) is a 4D film theme park attraction located at Universal Studios Japan, SeaWorld San Antonio, formerly at SeaWorld San Diego, Busch Gardens Williamsburg and Busch Gardens Tampa Bay.  The attraction, which was made to run at Universal Studios Japan, was later acquired by SeaWorld Parks and Entertainment to run at their Busch Gardens and SeaWorld theme parks.  In addition, Busch Gardens parks also include multiple other Sesame Street themed attractions, as part of their Sesame Street Forest of Fun/Sesame Street Safari of Fun park areas.  The attraction contains 4-D effects to go along with the film which include spraying water, bursts of air, leg ticklers and fans.

Jungle Cruise: The Jungle Cruise is an attraction located in Adventureland at many Disney Parks, including Disneyland, Magic Kingdom, and Tokyo Disneyland.  At Hong Kong Disneyland, the attraction is named Jungle River Cruise.  Disneyland Paris and Shanghai Disneyland are the only Magic Kingdom-style Disney parks that do not have the Jungle Cruise in their attraction rosters.

Walt Disney's Carousel of Progress: Walt Disney's Carousel of Progress is an attraction located at the Magic Kingdom park at the Walt Disney World Resort.  Created by both Walt Disney and WED Enterprises as the prime feature of the General Electric (GE) Pavilion for the 1964 New York World's Fair, the attraction was moved to Tomorrowland at Disneyland in Anaheim, California as Carousel of Progress, remaining there from 1967 until 1973.  It was replaced in Disneyland by America Sings in 1974, and reopened in its present home in Walt Disney World Resort's Magic Kingdom in 1975.

Cinderella Castle: Cinderella Castle is the fairy tale castle at the center of two Disney theme parks: the Magic Kingdom at the Walt Disney World Resort, and Tokyo Disneyland at the Tokyo Disney Resort.  Both serve as worldwide recognized icons and the flagship attraction for their respective theme parks.

Tomorrowland: Tomorrowland is one of the many themed lands featured at all of the Magic Kingdom styled Disney theme parks around the world owned or licensed by The Walt Disney Company.  Each version of the land is different and features numerous attractions that depict views of the future.  Disneyland Park in Paris includes a similar area called Discoveryland, which shares some elements with other Tomorrowlands but emphasizes visions of the future inspired by Jules Verne.

Liberty Square (Magic Kingdom): Liberty Square is one of six "themed lands" and is exclusive to the Magic Kingdom, a theme park at the Walt Disney World Resort in Lake Buena Vista, Florida.  Themed after colonial America, replicas of both the Liberty Bell and Liberty Tree can be seen here.  One of the most popular attractions in the Magic Kingdom, the Haunted Mansion, is located in this land.  Presiding over the square is the Hall of Presidents, an American history show featuring an audio-animatronic figure of every President of the United States.  Liberty Square has a long waterfront on the Rivers of America and the "Liberty Belle" Riverboat steam paddleboat departs from a landing here.  The land affords excellent views of the river and Tom Sawyer Island in adjacent Frontierland.

Epcot: Epcot (originally named EPCOT Center) is a theme park at the Walt Disney World Resort in Bay Lake, Florida.  It is owned and operated by the Walt Disney Company through its Parks and Resorts division.  Inspired by an unrealized concept developed by Walt Disney, the park opened on October 1, 1982 and was the second of four theme parks built at Walt Disney World, after the Magic Kingdom.  Spanning 300 acres , more than twice the size of the Magic Kingdom park, Epcot is dedicated to the celebration of human achievement, namely technological innovation and international culture, and is often referred to as a "permanent world's fair".  The park is divided into two sections: Future World, made up of eight pavilions, and World Showcase, themed to 11 world nations.

Wishes: A Magical Gathering of Disney Dreams: Wishes: A Magical Gathering of Disney Dreams was a fireworks show at the Magic Kingdom theme park of Walt Disney World.  The show debuted at the park on October 9, 2003, and was developed by Walt Disney Creative Entertainment, under the direction of VP Parades & Spectaculars, Steve Davison, who was assigned to create a replacement for the 32-year-old "Fantasy in the Sky" fireworks.  Several variations of the show at Walt Disney World include "Happy HalloWishes" during "Mickey's Not-So-Scary Halloween Party", "Holiday Wishes" during "Mickey's Very Merry Christmas Party", and "Magic, Music and Mayhem" during the 2007 event "Disney's Pirate and Princess Party".  The version at Disneyland Park in Disneyland Paris premiered on July 16, 2005 and had its final show on August 25, 2007.  The show at the Magic Kingdom was sponsored by Pandora Jewelry.  On February 9, 2017 it was announced by the Disney Parks Blog that "Wishes" would conclude its 13 year run at the Magic Kingdom.  The show was presented for the last time on May 11, 2017 at the Magic Kingdom Park and was replaced by "Happily Ever After" on May 12, 2017.

Question: Where is  an attraction located in of the many themed lands featured at all of the Magic Kingdom styled Disney theme parks that replaced an attraction called If You Could Fly?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "replaced_attraction_name": {
      "type": "string",
      "description": "The name of the attraction that was replaced."
    },
    "replacing_attraction_name": {
      "type": "string",
      "description": "The name of the attraction that replaced the old one."
    },
    "location_details": {
      "type": "object",
      "properties": {
        "themed_land": {
          "type": "string",
          "description": "The specific themed land where the attraction is located."
        },
        "park_name": {
          "type": "string",
          "description": "The name of the theme park."
        },
        "resort_name": {
          "type": "string",
          "description": "The name of the resort where the park is located."
        },
        "is_magic_kingdom_style_park": {
          "type": "boolean",
          "description": "Indicates if the park is a Magic Kingdom style theme park."
        }
      },
      "required": [
        "themed_land",
        "park_name",
        "resort_name",
        "is_magic_kingdom_style_park"
      ],
      "additionalProperties": false
    },
    "final_answer_location": {
      "type": "string",
      "description": "The top-level location that directly answers the question."
    }
  },
  "required": [
    "replaced_attraction_name",
    "replacing_attraction_name",
    "location_details",
    "final_answer_location"
  ],
  "additionalProperties": false
}
