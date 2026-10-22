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
Carl (name): Carl is a North Germanic male name meaning "strong man" or "free man".  The name originates in Scandinavia.  The name equates royal status; it is the first name of many Kings of Sweden including Carl XVI Gustaf.  It is popular in Denmark, Iceland, Finland, Norway, and Sweden, and was largely popularized in the United States by Scandinavian descendants.  Karl is a Germanic spelling which is very popular in Austria, Germany, Switzerland, and Norway, and was also popularized by German speaking descendants in the USA.  Other variants include the Anglo-Saxon-Frankish variant Charles, popular in Australia, Philippines, Canada, France, New Zealand, the UK and the United States; Carlo, very popular in Italy and southern Switzerland; Carlos, popular in Spain and Hispanic Latin America; and Karol, a variant in Poland and Slovakia.

Volvic (mineral water): Volvic is a brand of mineral water.  Its source is Clairvic Spring, Auvergne Regional Park just to the north of the Puy de Dôme in France.

Solo (Norwegian soft drink): Solo is an orange-flavoured soft drink, owned by the Norwegian companies Ringnes, Oskar Sylte, Aass, and Mack.  The recipe was originally Spanish, and brought to the Tønsberg Bryggeri by Torleif Gulliksrud in 1934.  Solo quickly became Norway's most popular soft drink, and until the 1960s was bigger than Coca-Cola in Norway.  In 1999, Pepsi passed Solo in market share, leaving Solo as third most popular.

Stage Dolls: Stage Dolls is a Norwegian hard rock band based in Trondheim, Norway.  In 1982, Erlend Antonsen and Terje Storli played at local clubs in and around Trondheim.  In need of a guitarist they called on Torstein Flakne, who by then had finished playing in The Kids (a popular teeny-band in Norway 1980-82).  Throughout the summer and fall of 1982 the newly formed band started rehearsing and playing shows in the region.  The trio took the name Stage Dolls in January 1983.  The first album, titled "Soldier's Gun", was released in the early winter of 1985 after a successful nationwide tour in Norway supporting the Norwegian band TNT.

Marit Larsen: Marit Elisabeth Larsen (born July 1, 1983) is a Norwegian singer and songwriter.  She began playing violin at age of 5 and played it until the age of 8.  She gained international fame during her teenage years as a member of the pop duo M2M with childhood friend Marion Raven.  She then pursued her own music career releasing her solo debut album, "Under the Surface", in 2006.  Her second album, "The Chase", was released in Norway in October 2008.  The third album, titled "Spark" was released in Norway, Denmark, Sweden, Finland on 18 November 2011 and Germany, Austria, Switzerland on 16 December 2011.  Her fourth studio album "When the Morning Comes" was released on 20 October 2014.  Larsen toured in its support within Norway with her own concerts, played songs from the album in Germany and Switzerland at public festivals and was the opening act at two of Johannes Oerding's concerts in November 2015.

Stabekk: Bærum has the highest income per capita and the highest proportion of university-educated individuals in Norway.  It is one of Norway's priciest and most fashionable residential areas, leading residents to be frequently stereotyped as snobs in Norwegian popular culture.  The area has some of the most conservative populace in Norway

Sjøgata: Sjøgata (Norwegian: 'Sea Street') is a historic and picturesque area running along the mouth of the river Vefsna in Mosjøen, a town in the traditional district of Helgeland in the county of Nordland, Norway.  Sjøgata, with the largest concentration of listed wooden buildings in northern Norway, is a popular tourist site.  Sjøgata is an area of piers, storehouses, boathouses, a number of galleries and several restaurants, together with the Vefsn museum and Kulturverkstedet, a culture workshop with exhibitions.  Sjøgata has been awarded the St. Olav Rose, the Norwegian Heritage Seal of Quality.  Fru Haugans Hotel, located on the end of Sjøgata, is the oldest hotel in North Norway dating back to a former trading post established in 1794.

Hilde Marie Kjersem: Hilde Marie Kjersem, also known as Marie Munroe, (born 27 April 1981 in Ålesund, Norway) is a Norwegian artist, musician and songwriter signed to Warner Music Norway.  She started out as a jazz musician, but has had an organic and natural development towards the world of pop.  In January 2016, Marie Munroe released her fourth solo album called "Under My Skin."  Munroe har been nominated for two Norwegian Grammy Awards (Spellemannprisen ), and has collaborated with some of Norway's most talented musicians - among them Sivert Høyem og Bernhoft.

Anne Grete Preus: Anne Grete Preus (born 22 May 1957 in Haugesund, Norway) is a Norwegian singer.  She was a rock artist in Norway in the 1980s and 1990s, first as member of the bands Veslefrikk and Can Can, and later as a solo artist.  She has released nine solo albums, and has won the Spellemannprisen and other awards multiple times.

Fatherland League (Norway): The Fatherland League (Norwegian: "Fedrelandslaget" ) was a right-wing, anti-communist political organisation in Norway.  Founded in 1925, the movement aimed to unite all centre-to-right forces against the rise of the revolutionary Marxist labour movement.  Organizing strikebreakers is one way they would prove to suffice.  At its peak of popular support and influence around 1930 it was the single largest mass movement ever organised on the political right in Norway, with estimated 100.000 members.  The movement began to decline through the 1930s, followed by some unsuccessful attempts to gain direct influence as a political party.  The Fatherland League was banned and dissolved upon the German occupation of Norway in 1940.

Question: Who is more popular in Norway, Volvic or Solo?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "comparison_topic": {
      "type": "string",
      "description": "The subject of the comparison, focusing on popularity in Norway."
    },
    "compared_items": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The names of the items being compared for popularity."
    },
    "most_popular_item_in_norway": {
      "type": "string",
      "description": "The item identified as more popular in Norway based on the provided context."
    },
    "item_popularity_data": {
      "type": "array",
      "description": "Detailed information about the popularity of each item in Norway, if available in the context.",
      "items": {
        "type": "object",
        "properties": {
          "item_name": {
            "type": "string",
            "description": "The name of the item."
          },
          "is_popular_in_norway": {
            "type": "boolean",
            "description": "Indicates if the item is explicitly stated as popular in Norway."
          },
          "popularity_description": {
            "type": "string",
            "description": "A summary of the item's popularity in Norway as described in the context."
          },
          "market_share_rank_in_norway": {
            "type": "integer",
            "description": "The market share rank of the item in Norway, if specified."
          },
          "historical_peak_popularity": {
            "type": "string",
            "description": "Description of the item's historical peak popularity in Norway, if specified."
          }
        },
        "required": [
          "item_name"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "comparison_topic",
    "compared_items",
    "most_popular_item_in_norway",
    "item_popularity_data"
  ],
  "additionalProperties": false
}
