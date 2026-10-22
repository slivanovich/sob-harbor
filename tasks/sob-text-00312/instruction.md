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
Tritheledontidae: The Tritheledontidae or tritheledontids, also known as ictidosaurs, were small to medium-sized (about 10 or 20 cm long) cynodonts.  They were extremely mammal-like, highly specialized cynodonts, although they still retained a very few reptilian anatomical traits.  Tritheledontids were mainly carnivorous or insectivorous, though some species may have developed omnivorous traits.  Their skeletons show that they had a close relationship to mammals. Tritheledontids or their closest relatives may have given rise to primitive mammals.  The tritheledontids were one of the longest lived non-mammalian therapsid lineages, living from late Triassic to the Jurassic period.  Tritheledontids became extinct in the Jurassic period, possibly due to competition with prehistoric mammals such as the triconodonts.  They are known from finds in South America and South Africa, indicating that they may have lived only on the supercontinent of Gondwana.  The family Tritheledontidae was named by South African paleontologist Robert Broom in 1912.  The family is often misspelled "Trithelodontidae".

Ishi: Ishi (c. 1861 – March 25, 1916) was the last known member of the Yahi, a group of the Yana of the U.S. state of California.  Widely acclaimed in his time as the "last wild Indian" in America, Ishi lived most of his life completely outside Euro-American culture.  At 50 years of age, in 1911, he emerged near the present-day foothills of Lassen Peak, also known as "Wa ganu p'a".

Nazlet Khater: Nazlet Khater is an archeological site located in Upper Egypt.  Excavations at the Nazlet Khater 2 site (Boulder Hill) yielded the remains of two human skeletons.  One of the skulls was that of a male subadult.  The cranium was generally modern in form, but evinced some archaic traits in the temple and mandible areas.  Below the skull, the skeleton was robust but otherwise anatomically modern.  Morphological analysis of the Nazlet Khater mandible indicates that the specimen was distinct from the examined Late Pleistocene and Holocene North African specimens.  The Nazlet Khater 2 skeleton possesses two plesiomorphic features in its mandible, which are not found among coeval anatomically modern humans.  This suggests that the specimen's ancestors may have interbred with neighboring late archaic humans.  At Nazlet Khater 4 to the southeast, Upper Paleolithic axes, blades, burins, end scrapers and denticulates were also excavated.  The site has been radiocarbon dated to between 30,360-35,100 years ago.The similarities between NK2 and Upper Paleolithic European samples may indicate a close relationship between this Nile Valley specimen and European Upper Paleolithic modern humans.

Barbera Sarda: Barbera Sarda is a red Italian wine grape variety that is grown on the island of Sardinia where it often used to add acidity to blends.  Despite the similarities in their names, there is no known close genetic relationship between the Sardinian Barbera and the notable Piedmontese wine grape variety Barbera.  Nor does there seem to be any close relationship with other grapes names Barbera, such as Barbera bianca and Barbera del Sannio.

Anthony Saxton: Anthony Nicholas Scott Saxton (23 July 1934 – 31 March 2015) was a British advertising man and later headhunter who established the "swinging mega-boutique" "Way In" on the top floor of Harrods in 1967.  In 1979 he moved into the headhunting business Saxton Bampfylde.  He was chairman of executive search company Moloney and director of Australian miners Kingstream through which he formed close ties with the regime in North Korea.

Bernardin Gantin: Bernardin Gantin (8 May 1922 – 13 May 2008) was a prominent Beninese cardinal of the Roman Catholic Church.  He served as Metropolitan Archbishop of the Roman Catholic Archdiocese of Cotonou and then at the Vatican in the service of the Holy See as President of the Pontifical Council for Justice and Peace and then as Prefect of the Sacred Congregation for Bishops.  Ultimately, he served as Dean of the Sacred College of Cardinals, a post his French consecrator as a bishop once held and the same position Joseph Ratzinger had after Gantin and before his election as Pope Benedict XVI.  He was the highest ranking Catholic to come from Africa since ancient times, when some Popes were believed to have come from there.  He enjoyed a close relationship with Pope John XXIII, Popes Paul VI and John Paul I, and most especially, with Pope John Paul II and his fellow curial cardinal and future Pope, Joseph Ratzinger.  Like many senior African prelates of his era, he was relatively conservative, but was esteemed by both his native land and for his work in Rome.  His tomb in Ouidah, which is frequently visited, was visited personally by Pope Benedict during the Papal Visit to Benin.  In May 2013, Vatican officials inaugurated a Chair about "Socializing Policy in Africa" bearing his name at the Pontifical Lateran University.

Portugal–United Kingdom relations: British–Portuguese relations are foreign relations between Portugal and the United Kingdom.  The relationship, largely driven by the nations' common interests as maritime countries on the edge of Europe and close to larger continental neighbours, dates back to the Middle Ages in 1373 with the Anglo-Portuguese Alliance.  The two countries now enjoy a healthy and close relationship.

Pio Laghi: Pio Laghi (21 May 1922 – 11 January 2009) was an Italian Cardinal of the Catholic Church.  His service was primarily in the diplomatic service of the Holy See and the Roman Curia.  He served as Apostolic nuncio to several countries and as the Prefect of the Congregation for Catholic Education.  He was elevated to the cardinalate in 1991.  Cardinal Laghi was Pope John Paul II's secret emissary to the White House and to several presidents of the United States.  He had a particularly close relationship with George H.W. Bush, and George W. Bush.

Bongseonsa: Bongseonsa is a head temple of the Jogye Order of Korean Buddhism.  It stands in Jinjeop-eup, Namyangju, a short distance east of Seoul in Gyeonggi province, South Korea.  It was built by National Preceptor Beobin in 969, under the Goryeo dynasty.  At that time it bore the name "Unaksa."  The current name dates to 1469, when Queen Jeonghui of the Joseon Dynasty changed the temple's name at the time that her husband King Sejo was buried nearby.  The name can be interpreted as "temple of revering the sage."  Thereafter, the temple continued to have a close relationship with the queens of Joseon.

Saxton Pope: Saxton Temple Pope (September 4, 1875 – August 8, 1926) was an American doctor, teacher, author and outdoorsman.  He is most famous as the father of modern bow hunting, and for his close relationship with Ishi, the last member of the Yahi tribe and the last known American Indian to be raised largely isolated from Western culture.

Question: Saxton Temple Pope had a close relationship with a man who lived most of his life where?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_of_interest": {
      "type": "string",
      "description": "The name of the person whose relationship is being described."
    },
    "related_person": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the person related to the person of interest."
        },
        "description": {
          "type": "string",
          "description": "A brief description of the related person."
        },
        "life_context": {
          "type": "string",
          "description": "The context or location where the related person lived most of their life."
        }
      },
      "required": [
        "name",
        "description",
        "life_context"
      ],
      "additionalProperties": false
    },
    "relationship_strength": {
      "type": "string",
      "description": "Describes the nature or strength of the relationship between the two individuals."
    }
  },
  "required": [
    "person_of_interest",
    "related_person",
    "relationship_strength"
  ],
  "additionalProperties": false
}
