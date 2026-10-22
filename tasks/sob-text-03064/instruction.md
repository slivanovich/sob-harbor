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
Liverpool: Liverpool ( ) is a city in North West England, with an estimated population of 478,580 in 2015.  With its surrounding areas, it is the fifth-largest metropolitan area in the UK, with over 2.24 million people in 2011.  The local authority is Liverpool City Council, the most populous local government district within the metropolitan county of Merseyside and the largest within the Liverpool City Region.

Peshtigo Fire Museum: On October 8, 1871, a firestorm roared through Peshtigo and surrounding areas, killing over 2,000 people and destroying the entire city and its livelihood.  The Peshtigo Fire Museum preserves this heritage through storytelling, exhibits of artifacts from the fire, displays of the lifestyle at the time of the disaster, and a cemetery to memorialize those who died.  The museum is located adjacent to the Peshtigo Fire Cemetery, where the charred remains of over 350 people were buried in a mass grave.  The cemetery is listed on the National Register of Historic Places.  The memorial at the cemetery was the first official state historical marker authorized by the State Historical Society of Wisconsin.

Manchester Blitz: The Manchester Blitz (also known as the Christmas Blitz) was the heavy bombing of the city of Manchester and its surrounding areas in North West England during the Second World War by the Nazi German Luftwaffe.  Manchester was an important inland port and industrial city during the war, and Trafford Park in neighbouring Stretford was a major centre of war production.

Druid Hill Park: Druid Hill Park is a 745 acre urban park in northwest Baltimore, Maryland.  Its boundaries are marked by Druid Park Drive (north), Swann Drive and Reisterstown Road (west and south), and the Jones Falls Expressway / Interstate 83 (east).  Inaugurated in 1860, Druid Hill Park, a famed urban park, ranks with Central Park (begun in 1858) in New York City and Fairmount Park (1812) in Philadelphia as the oldest landscaped public parks in the United States.

Santiago Metropolitan Park: The Santiago Metropolitan Park is an urban park located within the city of Santiago, capital of Chile.  Consisting of the San Cristóbal, Chacarillas and Los Gemelos hills, and the areas of Tupahue, Lo Saldés, Pirámide and Bosque Santiago, the park is located between four communes of Santiago - Huechuraba, Providencia, Recoleta and Vitacura - and covers around 722 hectares, making it the largest urban park in Chile and one of the largest in the world.

Kensal Green: Kensal Green is an area of north west London located on the southern boundary of the London Borough of Brent and the northern boundary of the Royal Borough of Kensington and Chelsea.  The surrounding areas are Harlesden to the west, Willesden to the north, Brondesbury and Queens Park to the east with Ladbroke Grove and White City to the south.  The areas of College Park and Kensal Green Cemetery are located in the London boroughs of Hammersmith & Fulham and Kensington & Chelsea, respectively.  The area has numerous transport links and is located close to the site of Old Oak Common.

North East England devolution referendum, 2004: The North East England devolution referendum was an all postal ballot referendum that took place on 4 November 2004 throughout North East England on whether or not to establish an elected assembly for the region.  Devolution referendums in the regions of Northern England were initially proposed under provisions of the Regional Assemblies (Preparations) Act 2003.  Initially, three referendums were planned, but only one took place.  The votes concerned the question of devolving limited political powers from the UK Parliament to elected regional assemblies in North East England, North West England and Yorkshire and the Humber respectively.  Each were initially planned to be held on 4 November 2004, but on 22 July 2004 the planned referendums in North West England and in Yorkshire and the Humber were postponed, due to concerns raised about the use of postal ballots, but the referendum in North East England was allowed to continue, particularly as it was assumed that the region held the most support for the proposed devolution.

List of castles in Cheshire: There are 20 castles in the county of Cheshire in North West England.  Cheshire is one of the historic counties of England and its historic boundaries are different from the modern county lines.  Some castles that were formerly in Cheshire are now in Greater Manchester.  In addition, Warrington Castle is historically a part of Lancashire but is within the current boundaries of Cheshire.  Before the Norman conquest of England began in 1066, defensive sites in England were communal, such as Anglo-Saxon burhs built as a defence against the Danes.  Castles were popularised in England by the Normans – although a few sites in the south-east pre-dating the Norman conquest – and were owned by the feudal lords.  The primary purpose of a castle was military: to be used as a base of operations and to control the surrounding areas.  A castle was considered to be a stamp of authority over the population of an area, and a status symbol.  Some would have acted as centres of trade and administration for a manor.

Sutton Park: Sutton Park is a large urban park located in Sutton Coldfield, Birmingham, West Midlands, England.  Most of the park is a National Nature Reserve; large parts are also a Scheduled Ancient Monument.  It is the largest urban park in Europe and the second largest outside a capital city.  The park covers more than 2400 acre , with a mix of heathland, wetlands and marshes, seven lakes, extensive ancient woodlands (covering approximately a quarter of the park), several restaurants, a private 18-hole golf course on its western edge and a municipal golf course to the south, a donkey sanctuary, children's playgrounds and a visitors' centre.  There is no entrance charge, although on summer Sundays a parking charge for cars applies.  A wide range of leisure activities are undertaken in the park including dog walking, pony treking, bike riding and kite flying.  There are areas to fly model aeroplanes and helicopters.  A railway line runs through the park.

St James Cemetery: St James's Cemetery is an urban park behind Liverpool Cathedral that is below ground level.  Until 1825, the space was a stone quarry, and until 1936 it was used as the Liverpool city cemetery.  It has been designated a Grade I Historic Park by Historic England.

Question: This urban park was used as a cemetery by a city in in North West England which with its surrounding areas is the fifth largest what in the UK?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "park_name": {
      "type": "string",
      "description": "The name of the urban park."
    },
    "city_info": {
      "type": "object",
      "properties": {
        "city_name": {
          "type": "string",
          "description": "The name of the city where the park is located."
        },
        "region": {
          "type": "string",
          "description": "The region of England where the city is located."
        },
        "metropolitan_area_rank": {
          "type": "integer",
          "description": "The ranking of the city's metropolitan area in the UK."
        },
        "metropolitan_area_type": {
          "type": "string",
          "description": "The type of area the city is ranked as (e.g., metropolitan area)."
        }
      },
      "required": [
        "city_name",
        "region",
        "metropolitan_area_rank",
        "metropolitan_area_type"
      ],
      "additionalProperties": false
    },
    "park_former_use": {
      "type": "string",
      "description": "The former use of the urban park."
    }
  },
  "required": [
    "park_name",
    "city_info",
    "park_former_use"
  ],
  "additionalProperties": false
}
