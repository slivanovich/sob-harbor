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
Rockhampton: Rockhampton is a city in the Rockhampton Region, Queensland, Australia.  The estimated urban population of Rockhampton in June 2015 was 80,665, making it the fourth largest regional city in the state outside of the cities of South East Queensland.  Rockhampton hosts a significant number of governmental, community and major business administrative offices for the central, coastal part of the state.

Great Barrier Reef Airport: Great Barrier Reef Airport or Hamilton Island Airport (IATA: HTI, ICAO: YBHM) is the primary airport of the Whitsunday Islands Group, and the airport of Hamilton Island.  The airport is settled on mostly reclaimed land and due the island's tourism status, is occupied mostly and favoured by Australia's leading low-cost airlines (Jetstar Airways and Virgin Australia) and Qantas.  Hamilton Island Airport handles direct flights from Sydney, Melbourne, Brisbane and Cairns and is also the airport launch pad for scenic flights to the Great Barrier Reef and Whitehaven Beach.  Private flights and charters also fly into Great Barrier Reef Airport, along with locally operated helicopters, light planes and seaplanes.

John F. Kennedy International Airport: John F. Kennedy International Airport (IATA: JFK, ICAO: KJFK, FAA LID: JFK) , often referred to as Kennedy Airport, or simply JFK, is the primary international airport serving New York City.  It is the busiest international air passenger gateway into North America, the fifth busiest airport in the United States and the busiest airport in the New York City airport system, handling just under 59 million passengers in 2016.  Over ninety airlines operate out of the airport, with non-stop or direct flights to destinations in all six inhabited continents.

Multan International Airport: Multan International Airport (Urdu: ‎ ) (IATA: MUX, ICAO: OPMT) is situated 4 km west of the city Multan in Punjab, Pakistan.  The airport is southern Punjab's largest and busiest airport.  Multan International Airport offers flights throughout Pakistan, as well as direct flights to Bahrain, Oman, Qatar, Saudi Arabia, and the United Arab Emirates.

International air travel from the United Kingdom: International air travel from the United Kingdom refers to the commercial carriage of passengers between the UK and the rest of the world.  In 2008, London Heathrow Airport which is also the busiest international airport on Earth handled 67,054,745 passengers which is more than the total population of the United Kingdom.  The 20 busiest airports in the UK handled close to 230 million passengers in 2008 (185 million of whom were international passengers).  The geographical size of the UK means that many flights that would be considered domestic in for example the United States are actually international (i.e. the distance from Heathrow to Charles de Gaulle Airport is roughly the same as the distance between John F. Kennedy International Airport and Washington Dulles International Airport).  The London airports, Heathrow, Gatwick and Stansted alongside Manchester Airport rank amongst the world's busiest airports by international passenger traffic.  According to 2008 statistics the best served nations by direct flights from the UK were France, Italy, Spain, the United States and Germany with 50, 34, 33, 31 and 29 respectively.  Overall Spain was the nation that saw the most passengers arrive from the UK in 2008, with a total of 34,557,729 (almost double the number that flew to the United States)

Brisbane: Brisbane ( ) is the capital of and most populous city in the Australian state of Queensland, and the third most populous city in Australia.  Brisbane's metropolitan area has a population of 2.4 million, and the South East Queensland region, centred on Brisbane, encompasses a population of more than 3.5 million.  The Brisbane central business district stands on the original European settlement and is situated inside a bend of the Brisbane River, about 15 km from its mouth at Moreton Bay.  The metropolitan area extends in all directions along the floodplain of the Brisbane River Valley between Moreton Bay and the Great Dividing Range, sprawling across several of Australia's most populous local government areas (LGAs), most centrally the City of Brisbane, which is by far the most populous LGA in the nation.  The demonym of Brisbane is Brisbanite.

Yinchuan Hedong International Airport: Yinchuan Hedong International Airport (IATA: INC, ICAO: ZLIC) is the primary airport serving Yinchuan, the capital of Ningxia Hui Autonomous Region, People's Republic of China.  It is located 25 km southeast of downtown Yinchuan in the town of Linghe of Lingwu City.  A relatively small airport compared to many airports in China, it nevertheless is the autonomous region's main aviation gateway.  Its name "Hedong" literally means "East of the River" and derives from the airport's location east of the Yellow River.  It is connected to over 20 cities by either direct flights, or transferring in Xi'an and Beijing.  The terminal building covers a total area of 15,000 m2 .  In 2013, the airport handled 4,247,843 passengers, making it the 39th-busiest airport in China.

Rourkela Airport: Rourkela Airport (IATA: RRK, ICAO: VERK) is a private airport located near Chhend Colony, 6 kilometres west of the steel city of Rourkela in the state of Odisha.  It is the only airport of the Metropolitan area of Rourkela city.  It is mostly used by dignitaries visiting Rourkela, especially officials of Steel Authority of India Limited(SAIL) and other V.I.Ps.The planes from this airport also travel to the city of Kolkata.  It is now ready to several direct flights within India.  Its terminus is now under the preparation for the proper facilities.

Kahramanmaraş: Kahramanmaraş is a city in Akdeniz, Turkey (the Mediterranean Region) and the administrative center of Kahramanmaraş Province.  Before 1973, Kahramanmaraş was named Marash.  The city lies on a plain at the foot of the Ahir Dağı (Ahir Mountain) and has a population of 1,112,634 as of 2017. The region is best known for its production of salep, a flour made from dried orchid tubers, and its distinctive ice cream.  It is connected by air to Istanbul and Ankara.  Turkish Airlines has daily direct flights from İstanbul and also AnadoluJet operates direct flights from Ankara.

Rockhampton Airport: Rockhampton Airport ("Connor Park") (IATA: ROK, ICAO: YBRK) is a major Australian regional airport in West Rockhampton that services the city of Rockhampton, with direct flights to the cities of Brisbane, Townsville, Gold Coast and Mackay.  It also operates connecting flights to the cities of Townsville and Cairns.  The Airport previously operated direct flights to Sydney and Melbourne but were cancelled due to lack of passenger numbers.  The Airport runway has the capability to handle aircraft such as the A380, B747 & B777 types.

Question: What is the population of a city where Rockhampton Airport has direct flights to 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "airport_name": {
      "type": "string",
      "description": "The name of the airport in question."
    },
    "destination_cities": {
      "type": "array",
      "description": "A list of cities that the airport has direct flights to.",
      "items": {
        "type": "string"
      }
    },
    "target_city_name": {
      "type": "string",
      "description": "The name of the specific city whose population is being requested."
    },
    "target_city_population": {
      "type": "number",
      "description": "The population of the target city."
    },
    "population_unit": {
      "type": "string",
      "description": "The unit of measurement for the population (e.g., 'million', 'thousand')."
    }
  },
  "required": [
    "airport_name",
    "destination_cities",
    "target_city_name",
    "target_city_population",
    "population_unit"
  ],
  "additionalProperties": false
}
