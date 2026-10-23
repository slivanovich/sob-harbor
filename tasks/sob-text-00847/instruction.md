{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCalifornia-style pizza: California-style pizza (also known as California pizza or Gourmet pizza) is a style of single-serving pizza that combines New York and Italian thin crust with toppings from the California cuisine cooking style.  Its invention is generally attributed to chef Ed LaDou, and Chez Panisse, in Berkeley, California.  Wolfgang Puck, after meeting LaDou, popularized the style of pizza in the rest of the country.  It is served in a number of California Cuisine restaurants.  Such restaurant chains as California Pizza Kitchen, Extreme Pizza, and Sammy's Woodfired Pizza are three major pizza franchises associated with California-style pizza.  Nancy Silverton's Pizzeria Mozza is also a popular California-style pizza restaurant in Los Angeles.\n\nList of Two Guys and a Girl episodes: The following is a list of episodes for the television show \"Two Guys, a Girl and a Pizza Place\" (retitled \"Two Guys and a Girl\" in its third season).  The show began its run on March 10, 1998, following two pizza delivery boys, Pete Dunville (Richard Ruccolo) and Michael \"Berg\" Bergen (Ryan Reynolds).  They are close friends with the feisty Sharon Carter (Traylor Howard), the spokesperson of Immaculate Chemicals.  The show aired on Wednesday nights for most of its run until it was moved to the Friday night death slot in 2000.  This resulted in a steep drop in ratings and the plug was pulled.  The series finale was titled \"The Internet Show,\" an episode where fans of the show could go online and vote for the outcome.  In the end, they chose to have Ashley become pregnant with Pete's child, as opposed to either of the other two female characters, or nobody, becoming pregnant.  Revelation Films released the complete series on region 2 DVD in the UK, 24 June 2013.\n\nRobert L. Brock: Robert L. Brock (c. 1924 – June 7, 1998) was an American businessman.  He was born in Pawnee Rock, Kansas and graduated from Sterling High School and Kansas University.  he started \"Inn Operations\" with a friend and sold it to Holiday Inns, Inc to manage \"Topeka Inn Management\".  As chairman of TIM (later renamed Brock Hotel Corporation), the first and at the time largest franchisee of Holiday Inns, he founded ShowBiz Pizza Place in 1980 in Topeka, Kansas after becoming a Pizza Time Theatre franchisee.  He also started The Residence line of hotels with Jack DeBoer.  Marriott later bought the brand and renamed all locations \"Residence Inn by Marriott\".\n\nChicago Franchise Systems, Inc.: Chicago Franchise Systems, Inc. franchises operates Italian-based Chicago-style restaurants in Illinois, Georgia, California and Missouri which specialize in Chicago-style cuisine They have operated since 1990, when they took over the popular Nancy's Pizza chain of pizzerias.  Nancy's itself was started in 1971 by Nancy and Rocco Palese, a couple who claims to have invented the concept of stuffed pizza.  Today, there are 36 Nancy's locations in Chicago metropolitan area, as well as two location in the Atlanta, Georgia area, and one in the Los Angeles, CA area.  CFS, Inc. operates Al's Beef, a popular Italian beef restaurant that is extremely well known in downtown Chicago and is regarded as one of the best beef sandwiches in the country.  CFS, Inc. just launched Doughocracy Pizza + Brews, a fast casual pizza place that gives customers the \"Freedom to Choose\" their own toppings on a hand stretched pizza crust that can be paired with local craft beers.  There are two Doughocracy restaurants, one in Geneva, Illinois and one in University City, Missouri, a suburb of St. Louis.\n\nFox's Pizza Den: Fox's Pizza Den is a pizzeria chain based in Murrysville, Pennsylvania, United States.  It was founded in 1971 by Jim Fox in Pitcairn, Pennsylvania, and currently has more than 250 locations in 28 U.S. states, all franchise-owned.  Fox's Pizza Den has consistently ranked among the Top 25 pizza chains in the world.  The Small Business Administration named Jim Fox as one of the country's top entrepreneurs during National Small Business Week, May 5–11, 2002.  Since that time, many Fox's Franchises have closed due to a poor business model.  The alarming rate of failure lead to the SBA discontinuing the lending of money for Fox's Franchises.  Fox's Pizza was ranked \"Best Pizza Franchise\" in 2007.\n\nThe Amazing Pizza Machine: The Amazing Pizza Machine is a family entertainment center located in the Millard area of Omaha, Nebraska.  According to \"Play Meter\" magazine, the Amazing Pizza Machine has an \"array of games, rides, and attractions all under one roof are unparalleled in the region.\"  The facility has received several industry awards, including being named a \"Top Family Entertainment Center of the World\" by the International Association of Amusement Parks and Attractions in 2007.  The Amazing Pizza Machine is owned in part by the co-owners of Valentino's Pizza.\n\nShowBiz Pizza Place: ShowBiz Pizza Place was a restaurant pizza chain and family entertainment center founded in 1980 by Robert L. Brock and Creative Engineering.  The brand emerged following a separation between Brock and Pizza Time Theatre, owners of the Chuck E. Cheese's franchise.  ShowBiz Pizza restaurants entertained guests through a large selection of arcade games, coin-operated rides, and animatronic stage shows as a way to provide a complete package of food and entertainment.\n\nThe Rock-afire Explosion: The Rock-a-fire Explosion is an animatronic robot band that played in Showbiz Pizza Place from 1980 to 1992, and in various Showbiz Pizza locations between 1990 and 1992 as Showbiz rebranded and the band was steadily replaced by Chuck E. Cheese characters.  The show was created and manufactured by inventor Aaron Fechter, creator of Whac-A-Mole, through his company Creative Engineering, Inc. in Orlando, Florida; in addition to overseeing the production of the animatronics, Fechter also provided the voices for several characters.\n\nVocelli Pizza: Vocelli Pizza (formerly Pizza Outlet) is a pizzeria based in Pittsburgh, Pennsylvania.  s of 2008 , the chain has stores in the District of Columbia, Florida, Maryland, North Carolina, Ohio, Pennsylvania, South Carolina, Virginia, and West Virginia.  The trade magazine \"Pizza Today\" ranked Vocelli Pizza in their Top 100 pizza franchises for 2007, based on its 2006 sales of $55 million.\n\nDonatos Pizza: Donatos Pizza is a pizza delivery restaurant chain headquartered in Columbus, Ohio.  It has nearly 200 locations in eight states, with the majority of locations in Ohio.  Donatos is also served at several venue outlets including Ohio Stadium and the Smithsonian National Air and Space Museum.\n\nQuestion: What pizza place was ranked in The trade magazine \"Pizza Today\" in their Top 100 pizza franchises for 2007,  Vocelli Pizza or Donatos Pizza?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"ranked_pizza_place_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the pizza place that was ranked.\"\n    },\n    \"ranking_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"source_magazine\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the trade magazine that published the ranking.\"\n        },\n        \"ranking_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the ranking was published or for which it was valid.\"\n        },\n        \"ranking_list_name\": {\n          \"type\": \"string\",\n          \"description\": \"The specific name of the ranking list (e.g., 'Top 100 pizza franchises').\"\n        }\n      },\n      \"required\": [\n        \"source_magazine\",\n        \"ranking_year\",\n        \"ranking_list_name\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"comparison_candidate_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the other pizza place mentioned in the question for comparison.\"\n    }\n  },\n  \"required\": [\n    \"ranked_pizza_place_name\",\n    \"ranking_details\",\n    \"comparison_candidate_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "ranked_pizza_place_name": {
        "type": "string",
        "description": "The name of the pizza place that was ranked."
      },
      "ranking_details": {
        "type": "object",
        "properties": {
          "source_magazine": {
            "type": "string",
            "description": "The name of the trade magazine that published the ranking."
          },
          "ranking_year": {
            "type": "integer",
            "description": "The year the ranking was published or for which it was valid."
          },
          "ranking_list_name": {
            "type": "string",
            "description": "The specific name of the ranking list (e.g., 'Top 100 pizza franchises')."
          }
        },
        "required": [
          "source_magazine",
          "ranking_year",
          "ranking_list_name"
        ],
        "additionalProperties": false
      },
      "comparison_candidate_name": {
        "type": "string",
        "description": "The name of the other pizza place mentioned in the question for comparison."
      }
    },
    "required": [
      "ranked_pizza_place_name",
      "ranking_details",
      "comparison_candidate_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
