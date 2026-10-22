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
List of Olympic Games host cities: This is a list of host cities of the Olympic Games, both summer and winter, since the modern Olympics began in 1896.  Since then, summer games have usually but not always celebrated a four-year period known as an Olympiad.  There have been 28 Summer Olympic Games held in 23 cities, and 22 Winter Olympic Games held in 19 cities.  In addition, three summer and two winter editions of the Games were scheduled to take place but later cancelled due to war: Berlin (summer) in 1916; Tokyo/Helsinki (summer) and Sapporo/Garmisch-Partenkirchen (winter) in 1940; and London (summer) and Cortina d'Ampezzo, Italy (winter) in 1944.  The 1906 Summer Olympics were officially sanctioned and held in Athens.  However, in 1949, the International Olympic Committee (IOC), decided to unrecognize the 1906 Games.  Five cities have been chosen by the IOC to host upcoming Olympic Games: Pyeongchang for the 2018 Winter Olympics, Tokyo for the 2020 Summer Olympics, Beijing for the 2022 Winter Olympics, Paris for the 2024 Summer Olympics, and Los Angeles for the 2028 Summer Olympics.

2022 Winter Olympics: The 2022 Winter Olympics, officially known as the XXIV Olympic Winter Games (French: "Les XXIVeme Jeux olympiques d'hiver" ) (), and commonly known as Beijing 2022, is a multi-sport event that will take place in Beijing and towns in the neighboring Hebei province, China from 4 to 20 February 2022.  It will be the third consecutive Olympic Games held in East Asia, after Pyeongchang 2018 and Tokyo 2020.  Having previously hosted the 2008 Summer Olympics, Beijing will become the first city to ever host both the Summer and the Winter Olympic Games.  It will also become the largest city ever to host the Winter Olympics, a distinction currently held by Vancouver which hosted the 2010 Winter Olympics.

Los Angeles bid for the 2024 Summer Olympics: The Los Angeles bid for the 2024 Summer Olympics and Summer Paralympics was the attempt to bring the Summer Olympic Games to the city of Los Angeles, California in 2024; the games were ultimately awarded to the city for 2028.  Following withdrawals by other bidding cities during the 2024 Summer Olympics bidding process that led to just two candidate cities (Los Angeles and Paris), the International Olympic Committee (IOC) announced that the 2028 Summer Olympics would be awarded at the same time as 2024.  After extended negotiations, Los Angeles agreed to bid for the 2028 Games if certain conditions were met.  On July 31, 2017, the IOC announced Los Angeles as the sole candidate for the 2028 games, with $1.8 billion of additional funding to support local sports and the Games program.

Great Britain at the 2012 Summer Olympics: Great Britain, represented by the British Olympic Association (BOA), competed at the 2012 Summer Olympics in London, United Kingdom, from 27 July to 12 August 2012 as the host nation.  British athletes have competed at every Summer Olympic Games in the modern era, alongside Australia, France and Greece, though Great Britain is the only one to have won at least one gold medal at all of them.  London is the only city to host the Summer Olympics on three different occasions, having previously done so in 1908 and 1948.  Soon, it will be joined by Paris in 2024 and Los Angeles in 2028 in hosting the Olympic Games for a third time.  Team GB, organised by BOA, sent a total of 541 athletes, 279 men and 262 women, to the Games, and won automatic qualification places in all 26 sports.

Budapest bid for the 2024 Summer Olympics: The Budapest bid for the 2024 Summer Olympics and Summer Paralympics was announced by the Hungarian Olympic Committee (Hungarian: "Magyar Olimpiai Bizottság, MOB" ) on 11 November 2013, although organisers had been planning a bid since 2008.  However, on 1 March 2017 Budapest withdrew its bid to host the 2024 Summer Olympics, leaving only Los Angeles and Paris in the race.

Paris bid for the 2024 Summer Olympics: The Paris bid for the 2024 Summer Olympics and Summer Paralympics is the successful bid to bring the Games of the XXXIII Olympiad and the XVII Paralympic Games, to the French capital city.  Paris formally announced its intention to bid on 23 June 2015 – the date on which Olympic Day is globally celebrated.  Following withdrawals in the 2024 Summer Olympics bidding process that led to just two candidate cities (Los Angeles and Paris), the IOC announced that the 2028 Summer Olympics would be awarded at the same time as the 2024 Games.  After Los Angeles agreed on 31 July 2017 to host the 2028 Games.  It was offically announced at the IOC Session in Lima, Peru.

2020 Summer Olympics closing ceremony: The closing ceremony of the 2020 Summer Olympics is scheduled to take place on the evening of Sunday August 9th, 2020 in the National Stadium.  The Olympic flag will be handed over from Tokyo to Paris, the host city of the 2024 Summer Olympics.

2024 Summer Olympics: The 2024 Summer Olympics (French: "Les Jeux olympiques d'été de 2024" ), officially known as the Games of the XXXIII Olympiad, and commonly known as Paris 2024, is a forthcoming international multi-sport event which will be hosted in Paris from 2 to 18 August 2024.  Having previously hosted the 1900 Summer Olympics and the 1924 Summer Olympics, Paris will become the second city after London (1908, 1948 and 2012) to host the Olympic Games three times.  2024 will also mark the centennial of the 1924 Summer Olympics, which were held in the same city, and was the last time Paris held the Olympic Games.

Hamburg bid for the 2024 Summer Olympics: The Hamburg bid for the 2024 Summer Olympics was a cancelled bid of Hamburg to host the 2024 Summer Olympics.

Rome bid for the 2024 Summer Olympics: The Rome bid for the 2024 Summer Olympics and Summer Paralympics was an attempt to bring the 2024 Summer Olympics to the city of Rome.  On 21 September 2016, Rome withdrew its bid for the Games.

Question: 2024 Summer Olympics will make Paris the second city ever to host the Summer Olympics three times. Which city is slated to become the third to hold this distinction?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "city_name": {
      "type": "string",
      "description": "The name of the city slated to host the Olympic Games for the third time."
    },
    "olympic_year": {
      "type": "integer",
      "description": "The year the city will host the Olympic Games for the third time."
    },
    "olympic_type": {
      "type": "string",
      "description": "The type of Olympic Games (Summer or Winter)."
    },
    "host_count": {
      "type": "integer",
      "description": "The total number of times the city will have hosted the Olympic Games."
    }
  },
  "required": [
    "city_name",
    "olympic_year",
    "olympic_type",
    "host_count"
  ],
  "additionalProperties": false
}
