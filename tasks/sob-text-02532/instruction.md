{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMarvel Superheroes Theme Park: Marvel Superheroes Theme Park is a future 100 acre Marvel indoor theme park in Dubailand that was expected to open in November 2014.  This park was originally announced in late 2007 by United-Emirate Based Al Ahli group theme park company and Marvel Entertainment.  On August 31, 2009, The Walt Disney Company bought Marvel for $4.24 billion and now controls the theme park rights to the company's characters.  Since the Universal Studios parks have Marvel-based attractions at Universal's Islands of Adventure Park in Florida and at Universal Studios Japan in Osaka, Japan, Universal owns the rights to have Marvel attractions East of the Mississippi River in the United States and in Japan, but not elsewhere.\n\nUniversal Studios South Korea: Universal Studios Korea (USK; 유니버설 스튜디오 코리아) is a cancelled theme park to constructed in the vicinity of Hwaseong, South Korea.  If the park was constructed, become the fifth Universal Studios theme park in the world, and the fourth in Asia, after Universal Studios Japan, Universal Studios Singapore, and Universal Studios Beijing upon its projected opening in 2020.  On 23 December 2015, Universal Studios Korea consortium led by China’s largest state-run builder, China State Construction Engineering Corporation, and its largest state-run tourist agency, China Travel Services, won the bidding for the project held by K-Water, the owner of the project site.  The consortium also includes the Korean construction firm Daewoo E&C and Korean engineering consulting firm Dohwa Engineering as well as Universal Studios Korea Property Holdings.\n\nIslands of Adventure: Universal's Islands of Adventure (formally Universal Studios Islands of Adventure, and commonly known as Islands of Adventure) is a theme park in Orlando, Florida.  It opened on May 28, 1999, along with CityWalk, as part of an expansion that converted Universal Studios Florida into the Universal Orlando Resort.  The slogan for this theme park, along with Universal Studios Florida, is \"Vacation Like You Mean It\", introduced in 2013 as Universal Orlando Resort.\n\nUniversal Studios Hollywood: Universal Studios Hollywood is a film studio and theme park in the San Fernando Valley area of Los Angeles County, California.  About 70% of the studio lies within the unincorporated county island known as Universal City while the rest lies within the city limits of Los Angeles, California.  It is one of the oldest and most famous Hollywood film studios still in use.  Its official marketing headline is \"The Entertainment Capital of LA\".  It was initially created to offer tours of the real Universal Studios sets and is the first of many full-fledged Universal Studios Theme Parks located across the world.\n\nUniversal Studios Singapore: Universal Studios Singapore (; Tamil: யுனிவர்சல் ஸ்டுடியோஸ், சிங்கப்பூர் ) is a theme park located within Resorts World Sentosa on Sentosa Island, Singapore.  It was a key component of Genting's bid for the right to build Singapore's second integrated resort.  On 8 December 2006, the Singapore government announced that the consortium had won the bid.  Construction of the theme park and the rest of the resort started on 19 April 2007.  It is the second Universal Studios theme park to open in Asia (Japan being the first), and the first in Southeast Asia.  The official plans for the park were unveiled to the public when Universal Studios Singapore released a park map to the public on 20 October 2009.  Universal Studios Singapore has since attracted more than 2 million visitors in the 9 months from its opening.\n\nHarry Potter and the Forbidden Journey: Harry Potter and the Forbidden Journey is a motion-based dark ride located in The Wizarding World of Harry Potter themed areas of Islands of Adventure in Orlando, Florida, Universal Studios Hollywood in Universal City, California, and Universal Studios Japan in Osaka, Japan.  The ride takes guests through scenes and environments in and around Hogwarts Castle from the Harry Potter series of books and films.  Mark Woodbury, president of Universal Creative, described the ride as an in-depth look at the world of Harry Potter, which utilizes never-before-seen technology which transforms \"the theme park experience as you know it\".  The ride first opened at Islands of Adventure with \"The Wizarding World of Harry Potter\" on June 18, 2010, at Universal Studios Japan on July 15, 2014, and at Universal Studios Hollywood on April 7, 2016.\n\nList of Universal Studios Orlando attractions: The Universal Orlando Resort is a theme park resort located in Orlando, Florida.  It features two theme parks, Universal Studios Florida and Islands of Adventure, built on 107 acre and 101 acre of land, respectively.  Both parks feature several attractions and shows based on movies produced by Universal Studios.  After several delays during construction, Universal Studios Florida opened to the public on June 7, 1990; however, several of the parks major attractions experienced frequent mechanical and technical problems, forcing the rides to close.  Eventually, Universal filed a lawsuit against the manufacturer of Jaws, an attraction that was based on the film.  Three years later, Universal announced the construction of a second theme park, Islands of Adventure, that officially opened on May 28, 1999.\n\nUniversal Studios Beijing: Universal Studios Beijing or Universal Beijing Resort is the upcoming Universal theme park in the Chinese capital of Beijing that will open around 2020.  The park would become the fifth Universal Studios theme park in the world, and the third in Asia, after Universal Studios Japan and Universal Studios Singapore.\n\nUniversal Parks &amp; Resorts: Universal Parks & Resorts, also known as Universal Studios Theme Parks or solely Universal Theme Parks, is the theme park subsidiary of NBCUniversal.  The subsidiary, headquartered in Orlando, Florida, operates Universal theme parks and resort properties around the world.  Universal Parks & Resorts is best known for attractions and lands based on famous classic and modern pop culture properties (movies, television, literature, cartoons, comics, video games, music, etc.) from not only NBCUniversal, but also third-party companies, for all of its parks.\n\nFlight of the Hippogriff: Flight of the Hippogriff is a junior roller coaster in The Wizarding World of Harry Potter section at three theme parks – Universal Studios Japan, Universal Studios Hollywood, and Islands of Adventure of Universal Studios Florida.  Designed by Universal Creative, the first installation opened at Islands of Adventure on June 18, 2010.  The new ride was a redesign of an existing roller coaster known as Flying Unicorn, which the park closed in 2008 to begin its transformation.  The design change was implemented to fit the new \"Harry Potter\" themed area that was being constructed at the park.  Flight of the Hippogriff is a mild alternative to the area's more extreme rides such as Dragon Challenge and Harry Potter and the Forbidden Journey.  Following a successful launch, identical versions of the roller coaster were installed at Universal Studios Japan and Universal Studios Hollywood over the next several years.\n\nQuestion: Universal Studios Korea, is a cancelled theme park to constructed in the vicinity of Hwaseong, South Korea, if the park was constructed, become the fifth Universal Studios theme park in the world, and the fourth in Asia, including Universal Studios Beijing, is the upcoming Universal theme park in the Chinese capital of Beijing that will open around which year?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"theme_park_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the Universal Studios theme park.\"\n    },\n    \"status\": {\n      \"type\": \"string\",\n      \"description\": \"The current status of the theme park (e.g., upcoming, cancelled, open).\"\n    },\n    \"location\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"city\": {\n          \"type\": \"string\",\n          \"description\": \"The city where the theme park is located or planned.\"\n        },\n        \"country\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the theme park is located or planned.\"\n        }\n      },\n      \"required\": [\n        \"city\",\n        \"country\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"projected_opening_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the theme park is projected to open.\"\n    },\n    \"projected_rank_in_world\": {\n      \"type\": \"integer\",\n      \"description\": \"The projected rank of the park globally among Universal Studios theme parks.\"\n    },\n    \"projected_rank_in_asia\": {\n      \"type\": \"integer\",\n      \"description\": \"The projected rank of the park in Asia among Universal Studios theme parks.\"\n    }\n  },\n  \"required\": [\n    \"theme_park_name\",\n    \"status\",\n    \"location\",\n    \"projected_opening_year\",\n    \"projected_rank_in_world\",\n    \"projected_rank_in_asia\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "theme_park_name": {
        "type": "string",
        "description": "The name of the Universal Studios theme park."
      },
      "status": {
        "type": "string",
        "description": "The current status of the theme park (e.g., upcoming, cancelled, open)."
      },
      "location": {
        "type": "object",
        "properties": {
          "city": {
            "type": "string",
            "description": "The city where the theme park is located or planned."
          },
          "country": {
            "type": "string",
            "description": "The country where the theme park is located or planned."
          }
        },
        "required": [
          "city",
          "country"
        ],
        "additionalProperties": false
      },
      "projected_opening_year": {
        "type": "integer",
        "description": "The year the theme park is projected to open."
      },
      "projected_rank_in_world": {
        "type": "integer",
        "description": "The projected rank of the park globally among Universal Studios theme parks."
      },
      "projected_rank_in_asia": {
        "type": "integer",
        "description": "The projected rank of the park in Asia among Universal Studios theme parks."
      }
    },
    "required": [
      "theme_park_name",
      "status",
      "location",
      "projected_opening_year",
      "projected_rank_in_world",
      "projected_rank_in_asia"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
