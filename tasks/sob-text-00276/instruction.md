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
Celebrate the Magic: Celebrate the Magic was a nighttime show at the Magic Kingdom park of Walt Disney World, that premiered on November 13, 2012.  It replaced "The Magic, the Memories and You" display, a similar show that ran at the Magic Kingdom and Disneyland from January 2011 to September 4, 2012.

Magic Kingdom Resort Area: The Magic Kingdom Resort Area includes five resorts located along the shores of the Seven Seas Lagoon and Bay Lake, near the Magic Kingdom at the Walt Disney World Resort.  The area began with the opening of Disney's Contemporary Resort, Disney's Polynesian Resort and Disney's Fort Wilderness Resort & Campground.  The Walt Disney World Monorail System connects Disney's Contemporary Resort, Disney's Polynesian Village Resort and Disney's Grand Floridian Resort & Spa to the Transportation and Ticket Center and the Magic Kingdom.

Magic Kingdom for Sale–Sold!: Magic Kingdom for Sale–Sold!  is a fantasy novel by American writer Terry Brooks, the first in his Magic Kingdom of Landover.  Written in 1986, it tells the story of how Ben Holiday, a talented but depressed Chicago trial lawyer, comes to be king of Landover, an otherworldly magical kingdom.  The book was re-released as part of a Landover omnibus in 2009.

Walt Disney Imagineering: Walt Disney Imagineering Research & Development, Inc. is the research and development arm of The Walt Disney Company, responsible for the creation, design, and construction of Disney theme parks and attractions worldwide.  Founded by Walt Disney to oversee the production of Disneyland, it was originally known as Walt Disney, Inc. then WED Enterprises, from the initials meaning "Walter Elias Disney", the company co-founder's full name.

Wishes: A Magical Gathering of Disney Dreams: Wishes: A Magical Gathering of Disney Dreams was a fireworks show at the Magic Kingdom theme park of Walt Disney World.  The show debuted at the park on October 9, 2003, and was developed by Walt Disney Creative Entertainment, under the direction of VP Parades & Spectaculars, Steve Davison, who was assigned to create a replacement for the 32-year-old "Fantasy in the Sky" fireworks.  Several variations of the show at Walt Disney World include "Happy HalloWishes" during "Mickey's Not-So-Scary Halloween Party", "Holiday Wishes" during "Mickey's Very Merry Christmas Party", and "Magic, Music and Mayhem" during the 2007 event "Disney's Pirate and Princess Party".  The version at Disneyland Park in Disneyland Paris premiered on July 16, 2005 and had its final show on August 25, 2007.  The show at the Magic Kingdom was sponsored by Pandora Jewelry.  On February 9, 2017 it was announced by the Disney Parks Blog that "Wishes" would conclude its 13 year run at the Magic Kingdom.  The show was presented for the last time on May 11, 2017 at the Magic Kingdom Park and was replaced by "Happily Ever After" on May 12, 2017.

Epcot: Epcot (originally named EPCOT Center) is a theme park at the Walt Disney World Resort in Bay Lake, Florida.  It is owned and operated by the Walt Disney Company through its Parks and Resorts division.  Inspired by an unrealized concept developed by Walt Disney, the park opened on October 1, 1982 and was the second of four theme parks built at Walt Disney World, after the Magic Kingdom.  Spanning 300 acres , more than twice the size of the Magic Kingdom park, Epcot is dedicated to the celebration of human achievement, namely technological innovation and international culture, and is often referred to as a "permanent world's fair".  The park is divided into two sections: Future World, made up of eight pavilions, and World Showcase, themed to 11 world nations.

Seven Seas Lagoon: The Seven Seas Lagoon is a man-made lake at the Walt Disney World Resort in Bay Lake, Florida, near Orlando.  Located south of the Magic Kingdom theme park, the Seven Seas Lagoon serves as a natural buffer between the Magic Kingdom and its parking lot and connects with the adjacent Bay Lake.  The lake reaches a depth of 14 feet.  The lagoon is used mainly for recreational boating, as well as by the resort's three Disney Transport ferryboats that transport guests between the Magic Kingdom and the Transportation and Ticket Center.

Magic Kingdom: Magic Kingdom is a theme park at the Walt Disney World Resort in Bay Lake, Florida, near Orlando.  Owned and operated by The Walt Disney Company through its Parks and Resorts division, the park opened on October 1, 1971, as the first of four theme parks at the resort.  Initialized by Walt Disney and designed by WED Enterprises, its layout and attractions are based on Disneyland Park in Anaheim, California, and is dedicated to fairy tales and Disney characters.

Once Upon a Time (Disney parks): Once Upon a Time is a nighttime spectacular at Tokyo Disneyland and Magic Kingdom.  Similar to "Celebrate the Magic" and "Disney Dreams! ", the Tokyo show premiered on May 29, 2014, and utilizes fireworks, lasers, fire, projection mapping, and searchlights during the 19-minute presentation.  The Magic Kingdom version is shorter and excludes the use of fire and lasers.

The Black Unicorn: The Black Unicorn is the second novel in the Magic Kingdom of Landover series by Terry Brooks, and the follow-up to "Magic Kingdom for Sale -- SOLD! ".  Published in 1987, the book revolves around the evil wizard Meeks attempting to wrest control of the kingdom from Ben Holiday, the High Lord, and the appearance of a mythical black unicorn in the kingdom.

Question: Who is the co-founder of the company that designed Magic Kingdom?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "theme_park_name": {
      "type": "string",
      "description": "The name of the theme park."
    },
    "designing_company": {
      "type": "object",
      "properties": {
        "current_name": {
          "type": "string",
          "description": "The current name of the company responsible for design."
        },
        "name_at_design_time": {
          "type": "string",
          "description": "The name of the company at the time of the park's design."
        }
      },
      "required": [
        "current_name",
        "name_at_design_time"
      ],
      "additionalProperties": false
    },
    "company_co_founder": {
      "type": "object",
      "properties": {
        "full_name": {
          "type": "string",
          "description": "The full name of the co-founder of the designing company."
        }
      },
      "required": [
        "full_name"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "theme_park_name",
    "designing_company",
    "company_co_founder"
  ],
  "additionalProperties": false
}
