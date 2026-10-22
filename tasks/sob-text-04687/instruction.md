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
Bert van Loo: Bert van Loo (Gulpen, 1946 - 2016) was a Dutch sculptor, who mainly worked with glass.  He was mainly active in the Netherlands and China.

Giuseppe Appiani: Giuseppe Appiani (1740–1812) was an Italian painter of the Neoclassic periods.  He was born in Vaprio d'Adda, near Milan, where he was mainly active.  His parents moved to Monza, where his first mentor was the painter Giovanni Maria Gariboldi.  At age 21, he moved to Milan, where he worked in the studios of Giorgi, and later Giuliano Traballesi.  He was active in restoration of paintings.  Another painter, Giuseppe Appiani (Porto, c. 1700-Triefenstein, c. 1785), was active in Germany.

Tel, Azerbaijan: Tel- is a village(municipality at Khachmaz Region) situated in the northern-eastern part of Azerbaijan Republic.situated near the Nabran village.  The nature of the village is consist of deep forest and steps rich with natural springs.  Mainly popular as touristic region.  near the village there is "Tel Bulaghi"(Spring Tel) tourism center mainly active in summer.  Population is more than 700.  Main activity is agriculture, farming and a little bit tourism services.  Nationality-Azerbaijanis, Lezgins, Tats.

Zair Azgur: Zair Isaakovich Azgur (1908-1995) was a Belarusian sculptor active during the Soviet period.  Born in Mogilev Governorate (now in Vitebsk Region, Belarus), he studied in that city from 1922 to 1925; from 1925 until 1928 he studied at the Vkhutein in Leningrad.  He first exhibited in 1923.  He was mainly active in Minsk, where among his projects was the creation of reliefs for the opera house.  He created a series of portrait busts of war heroes and military figures during the 1940s.  At the 1958 World's Fair in Brussels he won a silver medal for his work.  Monuments to his design were erected at Lugansk in 1947; Minsk in 1947; Borodino in 1949; Suzdal in 1950; and Leninogorsk - a monument to Vladimir Lenin - in 1957.  Later in his career he exhibited in Bucharest and Paris.

Vatos Locos: Vatos Locos (in English, "Crazy Dudes") is a Street gang.  Gangs using this name are active in several American states, Europe and Africa.  The Vatos Locos originated in East LA but have extended their presence to Florida, Fort Pierce, Florida.  They are mainly active in Fort Pierce's South 18th Street area by Delaware and around South 33rd Street and Orange Avenue.  They represent their gang affiliation with black bandanas worn in the back right pocket of their pants.  Their graffiti consists of "Vatos Locos," the Lowrider logo, or Lil Rob.  These images are also present in gang tattoos.  Vatos Locos are mainly Mexicans or Chicanos.  Their dress consists of black shirts and khaki pants or shorts, and jewelry of chains or crosses.  Most are supporters of the Oakland Raiders football team and show this by wearing similar colors.

Gabriel Zehender: Gabriel Zehender was a German painter and printer believed to have been born in Grossmausdorf, and active in Basel.  He has frequently been identified with the "monogrammist GZ", an artist known to have been active at about that time.  He was mainly active from 1527-1535 although the woodcut "Christ on the Cross between the Virgin and Saint John", is believed to date from 1515.

List of Greek Resistance organizations: During the period of the Axis Occupation of Greece in the Second World War, a multitude of Resistance organizations sprang up.  A May 1943 report of the Intelligence Bureau of the Greek government in exile mentioned 33 active groups, a number that increased to 79 in a joint British report of 17 October 1943.  According to some sources, the number was as high as 140.  These numbers include groups of vastly different natures, which can be roughly divided in three categories: the major organizations, which displayed significant regional or nationwide action, including guerrilla operations against the Occupation authorities; the small political groupings, mainly active in Athens, with a limited following and engaged mainly in political propaganda and small-scale sabotage; and a small number of groups focused on intelligence and sabotage operations, in direct cooperation with the British secret services in the Middle East.

Chiarissimo Fancelli: Chiarissimo d'Antonio Fancelli (died 1632) was an Italian sculptor and architect of the late-Mannerist and Baroque periods, mainly active in Tuscany.  Domenico Pieratti and Giovanni Battista Pieratti were his pupils.  It is unclear how he fits into the large pedigree of Tuscan sculptors including Cosimo and Luca Fancelli.

Cosimo Ulivelli: Cosimo Ulivelli (1625–1704) was an Italian painter of the Baroque period, active mainly in Florence.  He was a pupil of the painter Baldassare Franceschini.  He painted frescoes along the top of the wall of the nave of the church the Santissima Annunziata in Florence.

Florence: Florence ( ; Italian: "Firenze" ] ) is the capital city of the Italian region of Tuscany.  It is the most populous city in Tuscany, with 383,083 inhabitants in 2013, and over 1,520,000 in its metropolitan area.

Question: In 2013, what was the population of the city in which Cosimo Ulivelli was mainly active?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "artist_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the artist."
        },
        "main_activity_city": {
          "type": "string",
          "description": "The city where the artist was mainly active."
        }
      },
      "required": [
        "name",
        "main_activity_city"
      ],
      "additionalProperties": false
    },
    "city_population_data": {
      "type": "object",
      "properties": {
        "city_name": {
          "type": "string",
          "description": "The name of the city."
        },
        "year": {
          "type": "integer",
          "description": "The year for which the population data is provided."
        },
        "population": {
          "type": "integer",
          "description": "The population count of the city in the specified year."
        },
        "population_unit": {
          "type": "string",
          "description": "The unit of measurement for the population (e.g., inhabitants)."
        }
      },
      "required": [
        "city_name",
        "year",
        "population",
        "population_unit"
      ],
      "additionalProperties": false
    },
    "final_answer": {
      "type": "integer",
      "description": "The final numerical answer to the question, representing the population."
    }
  },
  "required": [
    "artist_details",
    "city_population_data",
    "final_answer"
  ],
  "additionalProperties": false
}
