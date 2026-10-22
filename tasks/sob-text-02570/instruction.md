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
Służewiec: Służewiec is a neighborhood in Mokotów district of Warsaw, Poland.  Its main significance is that it contains Poland's main horse racing track, Sluzewiec Racetrack, the home of the Warsaw Derby.

NCHA Super Stakes: The NCHA Super Stakes is the second jewel in the National Cutting Horse Association's annual Triple Crown.  It is held in April following the November/December NCHA World Championship Futurity and a few months before the NCHA Derby, which is held during the summer in conjunction with the NCHA Summer Spectacular.  The Super Stakes is an event for 4-year old horses while the Super Stakes Classic is for 5 and 6-year old horses.  The event is limited to the offspring of stallions that were previously nominated by paying a subscription fee, the majority of which is added back to the million purse offered in prize money.

Singapore Turf Club: The Singapore Turf Club was founded in 1842 as the Singapore Sporting Club to operate the Serangoon Road Race Course at Farrer Park.  It is today the only horse-racing club in Singapore and is part of the Malayan Racing Association (MRA), which also regulates the three Turf Clubs in Malaysia, the Selangor Turf Club, Penang Turf Club and Perak Turf Club.  The Singapore Turf Club is the only authorised operator of horse racing, and totalisator (horse betting) services in Singapore.  It is the agent and proprietary club of the Tote Board, Singapore, who manages and directs its donation of surplus funds for charitable purposes.  The first race was held on 23 February 1843 when prize money on offer was only $150.  In 1924, the Club changed its name to the Singapore Turf Club.  This was done to reflect its role as a horse racing club more accurately.  The Club moved to Bukit Timah in 1933 before relocating to its present location at the Singapore Racecourse at Kranji in 1999.  The racecourse is adjacent to Kranji MRT Station.

Horse Racing (video game): Horse Racing is an equestrian video game released by Mattel Electronics for its Intellivision video game console in 1980.  Although primarily a sports video game, "Horse Racing" was actually assigned to the Gaming Network, due to its pari-mutuel betting for placing bets on the horses during the game; the game houses 8 virtual Thoroughbred race horses residing in the fictional "Rainbow Thoroughbred Stables" at a fictional western Kentucky race track called "Plympton Downs" (based loosely on long-time sportscaster/Intellivision sales personality George Plimpton).  Each of the horses have differing racing abilities (front runner, pace keeper, come from behind, ...), and do vary from game time to game time (a horse with come from behind traits during one match may have front runner abilities during the next match).  These horses are known by their colors (instead of their post position numbers—unlike in regular horse racing).

Breeders' Stakes (SAJC): The Breeders' Stakes is a South Australian Jockey Club Group 3 Thoroughbred horse race for two-year-olds, over a distance of 1200 metres, held annually at Morphettville Racecourse in Adelaide, Australia during the autumn.  Total prizemoney is A$120,000.

Ruidoso Downs Race Track: Ruidoso Downs is a horse racing track in Ruidoso Downs, New Mexico.  The track hosts both Thoroughbred and Quarter Horse racing, notably the All American Futurity, the richest race in Quarter Horse racing.

Northlands Park: Northlands Park is the "Alberta A circuit" horse racing track at Northlands in Edmonton, Alberta.  The horse racing season generally consists of a spring harness (Standardbred) meet from February/March, a Thoroughbred meet from May/June to September/October and a fall harness meet to mid-December.  Northlands Park (formerly Northlands Spectrum) is the building name for the grandstand.  There are three dining areas on the second floor.  Colours is the main dining room overlooking the race track and has a seating capacity of 700.  Uplinks Theatre is the simulcast restaurant area and features 6 projection televisions and up to 26 different simulcast race broadcasts from North American tracks and Sha Tin in Hong Kong.  Playbook Lounge is open limited hours and is available for private functions, sports broadcast events (27 televisions) and private parties.  There are two other concessions on the second floor - Rock's and The Deli - that are open during live horse racing.

Hidden Valley Downs: Hidden Valley Downs was a half-mile horse racing track opened in 1966 located near Medora, Reno County, Kansas.  The privately owned bush track hosted informal American Quarter Horse, and Thoroughbred events.  Bush tracks are unregulated by state commissions and are noted for "anything goes" racing.  Many famous horses raced at the track including Kentucky Derby winner Black Gold (horse).  The track gained minor notoriety after Sports Illustrated magazine published an article about the track in the October 31, 1966 edition called Anything Goes in the Bush by Jack Olsen.

The Red Mile: The Red Mile is a horse racing track located in Lexington, Kentucky, United States.  The track hosts harness racing, a type of horse racing in which the horses must pull two-wheeled carts called sulkies while racing.  It is one of harness racing's most famous tracks and is located in the heart of the Bluegrass region, an area of Kentucky famous for horse breeding and racing.

Morphettville Racecourse: Morphettville Racecourse is the main horse racing track for the Australian state of South Australia.  It is situated in the Adelaide suburb of Morphettville, and is about 10 km from the Adelaide city centre.  It is home to the South Australian Jockey Club.

Question: What is the prize money for the event held at the main horse racing track for the Australian state of South Australia for two-year old horses?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "event_name": {
      "type": "string",
      "description": "The name of the horse racing event."
    },
    "racecourse_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the racecourse where the event is held."
        },
        "location": {
          "type": "string",
          "description": "The city and country where the racecourse is located."
        },
        "is_main_state_track": {
          "type": "boolean",
          "description": "Indicates if the racecourse is the main track for its state."
        }
      },
      "required": [
        "name",
        "location",
        "is_main_state_track"
      ],
      "additionalProperties": false
    },
    "horse_age_category": {
      "type": "string",
      "description": "The age category of horses participating in the event."
    },
    "prize_money": {
      "type": "number",
      "description": "The total prize money offered for the event."
    },
    "currency": {
      "type": "string",
      "description": "The currency of the prize money."
    }
  },
  "required": [
    "event_name",
    "racecourse_details",
    "horse_age_category",
    "prize_money",
    "currency"
  ],
  "additionalProperties": false
}
