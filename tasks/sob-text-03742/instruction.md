{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nWestern River Expedition: The Western River Expedition (WRE) is the name of a Disney attraction that was designed but never built.  It was to be a western themed boat ride, slated to appear in the northwestern section of Frontierland at the Magic Kingdom, a theme park at the Walt Disney World Resort in Lake Buena Vista, Florida United States.\n\nSpace Mountain (Magic Kingdom): Space Mountain is an indoor dark outer space-themed steel roller coaster at the Magic Kingdom theme park at the Walt Disney World Resort in Lake Buena Vista, Florida.  Opened on January 15, 1975, Space Mountain is the oldest operating roller coaster in the state of Florida, and is the original version of the iconic attraction that has since been replicated at all of The Walt Disney Company's Magic Kingdom-style theme parks worldwide, except for the Shanghai Disneyland Resort.  RCA helped fund Space Mountain's construction and sponsored the ride from 1975 to 1993; FedEx sponsored Space Mountain from 1994 to 2004.\n\nWalt Disney World: The Walt Disney World Resort is an entertainment complex in Bay Lake and Lake Buena Vista, Florida, near Orlando and Kissimmee, Florida.  Opened on October 1, 1971, the resort is owned and operated by Walt Disney Parks and Resorts, a division of The Walt Disney Company.  It was initially operated by Walt Disney World Company.  The property covers 27258 acres , featuring four theme parks, two water parks, twenty-seven themed resort hotels, nine non–Disney hotels, several golf courses, a camping resort, and other entertainment venues, including Disney Springs.\n\nLiberty Tree Tavern: Liberty Tree Tavern is a restaurant located in the Liberty Square section of the Magic Kingdom in Walt Disney World.  The restaurant has a colonial theme, specifically that of New England.  The menu includes tavern ham, pot roast, turkey, cheeseburger, and Boston cream pie.\n\nMickey's Pirate and Princess Party: Mickey's Pirate and Princess Party was a hard-ticketed (separate admission) event held throughout the months of January through June at the Magic Kingdom theme park at the Walt Disney World Resort in Lake Buena Vista, Florida outside Orlando.  A smaller version was also planned for Disneyland Paris Resort in 2011, but was cancelled.  This event combined two of The Walt Disney Company's franchises, the Disney Princess line and the \"Pirates of the Caribbean\" franchise.\n\nLiberty Square (Magic Kingdom): Liberty Square is one of six \"themed lands\" and is exclusive to the Magic Kingdom, a theme park at the Walt Disney World Resort in Lake Buena Vista, Florida.  Themed after colonial America, replicas of both the Liberty Bell and Liberty Tree can be seen here.  One of the most popular attractions in the Magic Kingdom, the Haunted Mansion, is located in this land.  Presiding over the square is the Hall of Presidents, an American history show featuring an audio-animatronic figure of every President of the United States.  Liberty Square has a long waterfront on the Rivers of America and the \"Liberty Belle\" Riverboat steam paddleboat departs from a landing here.  The land affords excellent views of the river and Tom Sawyer Island in adjacent Frontierland.\n\nGolden Oak at Walt Disney World Resort: Golden Oak at Walt Disney World Resort is a residential community within the Walt Disney World Resort in Lake Buena Vista, Florida.  It was designed by Walt Disney Imagineering and is owned and operated by a newly formed Disney subsidiary, Golden Oak Realty.  The first phase of development is located southeast of the Magic Kingdom Park in Bay Lake.  The area was named to pay homage to Walt Disney's Golden Oak Ranch in California.  The first few home sites were available for purchase in late 2010 and completed in late 2011.\n\nBest Western Lake Buena Vista Resort Hotel: The Best Western Lake Buena Vista Resort Hotel is a 325-room resort that is on the property of Walt Disney World Resort in Lake Buena Vista, Florida.  The resort is located across from the Disney Springs area.  The hotel originally opened in November 1972 as the Travelodge at Lake Buena Vista.  It was operated by Travelodge from 1972 through 1983, then in 1984 the resort became the Viscount Hotel and operated as such until 1988.  In 1989, it was reacquired by Travelodge.  In 2000, the Travelodge hotel switched over to become the Best Western Lake Buena Vista Resort Hotel.  The hotel was renovated in 2004 and has 2 outdoor pools.\n\nHilton Orlando Lake Buena Vista: The Hilton Orlando Lake Buena Vista is an AAA Four-Diamond hotel located adjacent to the Disney Springs complex located on Walt Disney World Resort property in Lake Buena Vista, Florida.  The 23 acre hotel, which opened in November 1983, is among seven hotels that make up the Disney Springs Resort Area.  The Disney Springs Resort Area Hotels are located on the property of the Walt Disney World Resort in Lake Buena Vista, Florida, but are not operated by Disney.\n\nEpcot: Epcot (originally named EPCOT Center) is a theme park at the Walt Disney World Resort in Bay Lake, Florida.  It is owned and operated by the Walt Disney Company through its Parks and Resorts division.  Inspired by an unrealized concept developed by Walt Disney, the park opened on October 1, 1982 and was the second of four theme parks built at Walt Disney World, after the Magic Kingdom.  Spanning 300 acres , more than twice the size of the Magic Kingdom park, Epcot is dedicated to the celebration of human achievement, namely technological innovation and international culture, and is often referred to as a \"permanent world's fair\".  The park is divided into two sections: Future World, made up of eight pavilions, and World Showcase, themed to 11 world nations.\n\nQuestion: What is the name of a restaurant a restaurant located in the Liberty Square,  one of six \"themed lands\" and is exclusive to the Magic Kingdom, a theme park at the Walt Disney World Resort in Lake Buena Vista, Florida\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"restaurant_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the restaurant.\"\n    },\n    \"location_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"themed_land\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the themed land where the restaurant is located.\"\n        },\n        \"theme_park\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the theme park where the themed land is located.\"\n        },\n        \"resort\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the resort where the theme park is located.\"\n        },\n        \"city\": {\n          \"type\": \"string\",\n          \"description\": \"The city where the resort is located.\"\n        },\n        \"state\": {\n          \"type\": \"string\",\n          \"description\": \"The state where the resort is located.\"\n        }\n      },\n      \"required\": [\n        \"themed_land\",\n        \"theme_park\",\n        \"resort\",\n        \"city\",\n        \"state\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"restaurant_theme\": {\n      \"type\": \"string\",\n      \"description\": \"The specific theme of the restaurant.\"\n    }\n  },\n  \"required\": [\n    \"restaurant_name\",\n    \"location_details\",\n    \"restaurant_theme\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "restaurant_name": {
        "type": "string",
        "description": "The name of the restaurant."
      },
      "location_details": {
        "type": "object",
        "properties": {
          "themed_land": {
            "type": "string",
            "description": "The name of the themed land where the restaurant is located."
          },
          "theme_park": {
            "type": "string",
            "description": "The name of the theme park where the themed land is located."
          },
          "resort": {
            "type": "string",
            "description": "The name of the resort where the theme park is located."
          },
          "city": {
            "type": "string",
            "description": "The city where the resort is located."
          },
          "state": {
            "type": "string",
            "description": "The state where the resort is located."
          }
        },
        "required": [
          "themed_land",
          "theme_park",
          "resort",
          "city",
          "state"
        ],
        "additionalProperties": false
      },
      "restaurant_theme": {
        "type": "string",
        "description": "The specific theme of the restaurant."
      }
    },
    "required": [
      "restaurant_name",
      "location_details",
      "restaurant_theme"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
