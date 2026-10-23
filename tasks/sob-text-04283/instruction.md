{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nReebok: Reebok is a global athletic footwear and apparel company, operating as a subsidiary of Adidas since 2005.  Reebok produces and distributes fitness, running and CrossFit sportswear including clothing and footwear.  It is the official footwear and apparel sponsor for Ultimate Fighting Championship (UFC), CrossFit, Spartan Race, and Les Mills.\n\nBekana Daba: Bekana Daba (born 29 July 1988 in Welega, Oromia Region) is an Ethiopian long distance runner who specialises in the 5000 metres and marathon distances.\n\nJudged trail ride: A Judged trail ride is a type of trail riding popular in the western United States where horses and riders are asked to travel a natural trail for a set distance (usually 10 to 15 miles) with occasional stops for the horse and rider team to negotiate an obstacle, usually with varying options for difficulty, with higher scores given for completing the more difficult version of each obstacle.\n\nGusher Marathon: The Gusher Marathon is an annual spring marathon held in Beaumont, Texas.  It was founded in 2010 by the local nonprofit organization Sports Society for American Health and sponsored by Exygon Gym and Baptist Hospitals.  The \"Gusher\" in Gusher Marathon refers to the 1901 discovery of oil at the spindletop salt dome in Beaumont.  The course is a flat, fast USATF Sanctioned and Certified, Boston Qualifier.  The course begins at the Montagne Center of Lamar University and tours much of Downtown Beaumont before returning to Lamar University.  \"The Gusher\" also offers 5K and half marathon distances in addition to the full marathon.  The 2011 marathon was moved to mid march to take advantage of cooler weather.\n\nSpartan Race: Spartan Race is a series of obstacle races of varying distance and difficulty ranging from 3 miles to marathon distances.  They are held in US and have been franchised to 14 countries including Canada, South Korea, Australia and several European countries.  The series include the Spartan Sprint, the Super Spartan, the Spartan Beast, and the Ultra Beast.  Spartan Race also has a military series, hosted on military bases.  There are also winter and team events.\n\nJason Mbote: Jason Mbote (born 5 January 1977) is a Kenyan athlete who specializes in long distance, especially half marathon and marathon distances.\n\nRun for Your Lives (obstacle racing): Run For Your Lives (RFYL) is a 3-5K obstacle course adventure run series created by Maryland-based Reed Street Productions (RSP).  Like other obstacle races, runners navigate through various terrain and physically challenging obstacles.  Unlike other obstacle races, runners try to dodge and escape from zombies roaming the course trying to grab flags from runners' flagbelts, similar to flag football.  The course was designed to incorporate zombies as well as SERE training learned by a RSP managing-member who is active-duty navy.  The inaugural race had about 12,000 attendees and was covered by multiple news sources.\n\nAustin Marathon: The Austin Marathon is an annual marathon held in Austin, Texas.  It was founded in 1991 by Freescale Semiconductor, who served as title sponsor for fifteen years.  The marathon was sponsored by AT&T in 2007 and 2008, but ran with no title sponsor in 2009.  From 2010 to 2013, the race was called the LIVESTRONG Austin Marathon.  Freescale returned as presenting sponsor in 2014 and 2015.  NXP Semiconductors and Freescale completed their merger in December 2015, with NXP becoming the presenting sponsor for 2016 and 2017.  The Austin Half Marathon and Austin Marathon 5K are also part of the event.  The Austin Marathon annually hosts runners from all 50 states and more than 20 countries around the world.  The Austin Marathon presented by NXP will take place on February 19, 2017.\n\nPittsburgh Marathon: The Dick's Sporting Goods Pittsburgh Marathon, commonly referred to as the Pittsburgh Marathon, is an annual marathon footrace held on the first Sunday in May in Pittsburgh, Pennsylvania in the United States.  The Marathon was first announced on October 3, 1984 with U.S. Steel and PNC Bank as sponsors.  From 1985 to 2003, the race was held annually and named the UPMC/City of Pittsburgh Marathon, although serious financial difficulty within the City of Pittsburgh municipal budget and UPMC's withdraw from title sponsor led to suspension of the race from 2004 to 2008.  In 2009, the event was revived with a new title sponsor, Dick's Sporting Goods, and renewed interest in the race.\n\nReebok advertising campaigns: Reebok International Limited is a global producer of athletic footwear, apparel, and accessories and is a subsidiary of Adidas.  The name comes from the Afrikaans/Dutch spelling of rhebok, an African antelope or gazelle.  The company, founded in 1895, was originally called Mercury Sports but was renamed Reebok in 1960.  The company's founders, Joe and Jeff Foster, found the name in a dictionary won in a race by Joe Foster as a boy; the dictionary was a South African edition, hence the spelling.  Primarily selling its products in the U.K., in 1979, Paul Fireman, a US sporting goods distributor, saw a pair of Reeboks at an international trade show and negotiated to sell them in North America.  Reebok has marketed itself using a variety of ad campaigns.\n\nQuestion: Reebok is the official footwear and apparel sponsor for a series of obstacle races of varying distance and difficulty ranging from 3 miles to marathon distances, and are held in the US and franchised in how many countries?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"sponsor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the sponsoring company.\"\n    },\n    \"event_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of event being sponsored.\"\n    },\n    \"event_name\": {\n      \"type\": \"string\",\n      \"description\": \"The specific name of the event series.\"\n    },\n    \"franchised_countries_count\": {\n      \"type\": \"integer\",\n      \"description\": \"The number of countries where the event series is franchised.\"\n    },\n    \"event_distances\": {\n      \"type\": \"string\",\n      \"description\": \"The range of distances for the event races.\"\n    }\n  },\n  \"required\": [\n    \"sponsor_name\",\n    \"event_type\",\n    \"event_name\",\n    \"franchised_countries_count\",\n    \"event_distances\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "sponsor_name": {
        "type": "string",
        "description": "The name of the sponsoring company."
      },
      "event_type": {
        "type": "string",
        "description": "The type of event being sponsored."
      },
      "event_name": {
        "type": "string",
        "description": "The specific name of the event series."
      },
      "franchised_countries_count": {
        "type": "integer",
        "description": "The number of countries where the event series is franchised."
      },
      "event_distances": {
        "type": "string",
        "description": "The range of distances for the event races."
      }
    },
    "required": [
      "sponsor_name",
      "event_type",
      "event_name",
      "franchised_countries_count",
      "event_distances"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
