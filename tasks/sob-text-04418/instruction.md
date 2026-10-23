{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMonster Nationals: Monster Nationals is the name of the monster truck series run by Image Promotions.  The series primarily consists of monster truck racing and freestyle in indoor arenas.  The events typically have only two parallel sets of cars on an empty concrete floor as a race track.  The event format is similar to those of the USHRA Thunder Nationals series, due to owner George Eisenhart being the former director of that series.  Trucks currently running in the series include Big Dawg, Lil' Miss Dangerous, Nitemare, Raminator, and Rammunition.  In previous years, Bigfoot also competed.  Unlike its USHRA counterpart, the Monster Nationals series runs indoor arena shows during the winter season and outdoor fairground shows during the summer.  Some monster trucks that are new to the Monster Nationals include Tailgator (Doug Noelke's newest creation), Holman's Beast and teammate truck Ironman, and more.  Returning trucks to the circuit include War Wagon, formerly owned by Jeff Cook who sold it to Andy Hoffman, and Samson, who ran the outdoor series in 2003 and 2007.  The Monster Nationals, along with intense monster truck racing, also features some extreme stunts and performances such as a jet-powered Jeep, a jet-powered recliner, FMX Freestyle, BMX Freestyle, and car-eating transformers.\n\nThunder Truck Rally: Thunder Truck Rally (released as Monster Trucks in Europe) is a monster truck racing video game developed by Reflections and published by Psygnosis where players select a monster truck or otherwise 4X4 vehicle equipped with monster truck tires and have the option of either racing or crushing cars in an arena.\n\nAdam Anderson (monster truck driver): Adam Anderson (born December 5, 1985, in Norfolk, VA) is an American professional monster truck driver.  He currently drives the monster truck \"Grave Digger\" on the USHRA Monster Jam circuit.  Adam is the son of Dennis Anderson, a monster truck driver and 4-time Monster Truck World Champion.  Adam currently resides in his home town of Powells Point, NC.\n\nTrucks and Tractor Power: Trucks and Tractor Power was a long running weekly television show on TNN featuring mud bogging, tractor pulling and monster trucks.  The show's original hosts were Stan Rhoads and former Bigfoot driver Rich Hooser, along with pit reporter Mike Goss.  Gary Lee replaced Stan Rhoads.  Army Armstrong later joined as a pit reporter, and later, when Hooser left the show, became color commentator.  The show initially began in 1989 as a vehicle for TNT Motorsports events, complimenting their ESPN show Powertrax and syndicated show Tuff Trax, and would typically alternate between truck and tractor pulls and monster trucks, with National Mud Racing Organization mud races intermittently.  After TNT was bought out by the United States Hot Rod Association in 1991, the show began primarily airing the Pendaliner Monster Truck Series and NMRO mud races held at Special Events' 4-Wheel and Off-Road Jamborees.  A frequent feature of these shows was a highlight segment of \"Tough Truck\" amateur off-road races near the end of the monster truck episodes.  The final season of Trucks and Tractor Power had Gary Lee as the host at the Monster Truck Thunder Drags, with Dave Rief, and later Tom Rivers, for the Jamborees.  At the end of the 1996 season, the Pendaliner cancelled their sponsorship of the monster truck series, causing the show to be subsequently cancelled.\n\nBlue Thunder (truck): Blue Thunder is a monster truck that raced in the USHRA Monster Jam series.  It was sponsored by the truck division of Ford Motor Company and Live Nation.  The truck has several similarities with the monster truck Bigfoot.  Some fans saw Blue Thunder as a replacement for Bigfoot in the Monster Jam series.  The truck had been moderately successful and won several major events during its existence.  However, it has not yet won a championship.  Blue Thunder is used by Ford Motor Company for promotional purposes along with competition.  The truck is currently driven by Matt Cody.  The truck did not compete in 2012 when Todd LeDuc moved to Metal Mulisha after driving Blue Thunder in 2011.  The truck was brought back in 2013 with a veteran driver, Dan Evans; who use to own and drive Destroyer, then Team Hot Wheels, as well as a new paint job.\n\nTeam Scream Monster Trucks: Team Scream is a monster truck race team based out of the Detroit area and races on the Monster Jam series.  The team is made up of five trucks, Avenger, Brutus, Wrecking Crew Spike Unleashed, The General (or The General Tire Truck), and Rage.  The team founder is Jim Koehler and he is also the driver of Avenger.  In 2003 the team won the Monster Jam World Finals in freestyle.  Avenger is the only truck on the Monster Jam series to compete in every single Monster Jam World Finals with the same driver and truck.  Koehler once again won the freestyle championship in 2011, after tying with nitro circus.\n\nDennis Anderson: Dennis Anderson (born October 24, 1960) is an American professional monster truck driver.  He is the creator, team owner, and former driver of \"Grave Digger\" on the USHRA Monster Jam circuit.  Anderson is from Kill Devil Hills, North Carolina, where he currently resides.\n\nAround the World in 80 Ways: Around the World in 80 Ways is an American reality show that aired on The History Channel.  The program followed television personality Rob Mariano and professional monster truck driver Dennis Anderson as they traveled around the world using 80 various forms of transportation.  The show was also broadcast in Southeast Asia on the Discovery Channel.\n\nMonster Truck Madness 2: Monster Truck Madness 2 is a monster truck racing video game developed by Terminal Reality and Edge of Reality, and published by Microsoft for Microsoft Windows 95, NT, and Nintendo 64 in 1998 and 1999.  It's a sequel to \"Monster Truck Madness\".  The Nintendo 64 version of the game was co-published with Rockstar and released as Monster Truck Madness 64.\n\nSudden Impact (truck): Sudden Impact is a monster truck currently racing in the USHRA Monster Jam series.  The truck was originally driven by John Seasock and has been to four World Finals under his command.  It is the first monster truck to implement a driveline blanket, made of Kevlar, which goes around the outside of the drive shaft loop to make sure that if the driveshaft breaks, the parts will not fly off the truck, possibly causing injury to fans and officials.  In 2010 the truck was driven by a new driver Ben Winslow.  He used to be George Balhan's crew chief.  Another new thing is that it is now called Ground Pounder.  The truck is currently driven by Mike Dufrene and Steven Hill and is the teammate to Amsoil Shock Therapy, driven by Jeremy Brady and Dave Radzierez.  In the past, it has been driven by Dufrene, Hill, Winslow, Seasock, Carl Van Horn, Jon Zimmer, Sean Duhon, David Brown, Chris Lagana, Kevin Kosala, Chris Ryan, John Killinger, David Fray, and Casey Ladelle.\n\nQuestion: Around the World in 80 Ways follows the exploits of the driver of which monster truck?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"show_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the reality show.\"\n    },\n    \"featured_person\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the person featured in the show.\"\n        },\n        \"role\": {\n          \"type\": \"string\",\n          \"description\": \"The role of the person in the context of monster trucks.\"\n        },\n        \"associated_monster_truck\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the monster truck associated with the featured person.\"\n        },\n        \"truck_role\": {\n          \"type\": \"string\",\n          \"description\": \"The specific role of the person regarding the monster truck (e.g., driver, creator).\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"role\",\n        \"associated_monster_truck\",\n        \"truck_role\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"monster_truck_series\": {\n      \"type\": \"string\",\n      \"description\": \"The monster truck series the associated truck competes in.\"\n    }\n  },\n  \"required\": [\n    \"show_name\",\n    \"featured_person\",\n    \"monster_truck_series\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "show_name": {
        "type": "string",
        "description": "The name of the reality show."
      },
      "featured_person": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the person featured in the show."
          },
          "role": {
            "type": "string",
            "description": "The role of the person in the context of monster trucks."
          },
          "associated_monster_truck": {
            "type": "string",
            "description": "The name of the monster truck associated with the featured person."
          },
          "truck_role": {
            "type": "string",
            "description": "The specific role of the person regarding the monster truck (e.g., driver, creator)."
          }
        },
        "required": [
          "name",
          "role",
          "associated_monster_truck",
          "truck_role"
        ],
        "additionalProperties": false
      },
      "monster_truck_series": {
        "type": "string",
        "description": "The monster truck series the associated truck competes in."
      }
    },
    "required": [
      "show_name",
      "featured_person",
      "monster_truck_series"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
