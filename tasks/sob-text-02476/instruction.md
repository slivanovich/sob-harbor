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
W. E. B. Du Bois High School: W. E. B. Du Bois High School of Environmental Science (officially referred to as W. E. B. Du Bois High School) is a public high school located in northeast Baltimore, Maryland.  The school is named after sociologist and civil-rights activist Dr. W. E. B. Du Bois.  The school is situated in the former Northern High School and shares the structure with the Reginald F. Lewis High School.

Mary Doria Russell: Mary Doria Russell (born August 19, 1950) is an American novelist.

Men at War: Men at War is a series of World War II novels created by W. E. B. Griffin in 1984.  More recently, the series newest novels were co-authored by his son, William E. Butterworth (under the name William E. Butterworth IV).  Originally, the series was written under the pseudonym of Alex Baldwin.  Some editions of the books listing Baldwin as the author contain cover blurb quotations, attributed to Griffin, praising the books (i.e., he is praising his pseudonymous work under another of his pseudonyms.)

The Sparrow (novel): The Sparrow (1996) is the first novel by author Mary Doria Russell.

Children of God (novel): Children of God is the second book, and the second science fiction novel, written by author Mary Doria Russell.  It is the sequel to the award-winning novel, "The Sparrow".

The Crisis: The CRISIS is the official magazine of the National Association for the Advancement of Colored People (NAACP).  It was founded in 1910 by W. E. B. Du Bois (editor), Oswald Garrison Villard, J. Max Barber, Charles Edward Russell, Kelly Miller, W. S. Braithwaite, and Mary Dunlop Maclean.  "The Crisis" has been in continuous print since 1910, and it is the oldest black publication in the world.  Today, "The Crisis" is "a quarterly journal of civil rights, history, politics and culture and seeks to educate and challenge its readers about issues that continue to plague African Americans and other communities of color."

The Presidential Agent series: The Presidential Agent series was written by military author, W. E. B. Griffin.  The series consists so far of eight novels, "By Order of the President", "The Hostage", "The Hunters", "The Shooters", "Black Ops", "The Outlaws", "Covert Warriors", and "Hazardous Duty".  Like the rest of his novels, Griffin uses military time, along with the address of the place, and the chapter titles are never started on a separate page.  The series is the author's latest.

Wedding Album (Leon and Mary Russell album): Wedding Album is a studio album by Leon Russell and his then wife, Mary Russell, otherwise known as Mary McCreary.  It was the first album released on Leon Russell's record label, Paradise Records, which was distributed by Warner Bros.  Records.  Leon and Mary Russell are also credited as producers of the album, with the exception of the final track, "Daylight", which was produced by its writer, Bobby Womack.

Battle of Calcasieu Pass: The Battle of Calcasieu Pass was a minor skirmish fought on May 6, 1864, at the mouth of the Calcasieu River in southwestern Louisiana, during the American Civil War.  It resulted in a Confederate victory.  The participants of the battle were Lt. Benjamin Loring and Lt. C. W. Lamson on the Union’s side, and Col. W. H. Griffin on the Confederate side.  The union brought along two naval vessels, the U.S.S Wave and the U.S.S Granite City.  The U.S.S Wave did not prove too effective during the battle and was captured early on, it was soon turned into a Confederate cargo ship.  The U.S.S Granite City was originally a confederate blockade vessel, but was captured in 1863 by the U.S.S Tioga (Union).  The U.S.S Granite City was now back in the hands of the Confederates.  Captain Joseph A. Brickhouse, a Confederate veteran, said, “We fought in the open prairie, bringing on the attack with four small pieces of artillery and less than 300 infantry, poorly armed, attacking in the open prairie two such boats as the Granite City and Wave - Union gunboats - and capturing them after an action of less than two hours and 40 minutes duration.”  He described his own forces (Confederate) as unprepared, and he stated that they still had an easy battle that was short in duration.  The Confederate forces in this battle were split up into five battalions.  The first battalion was Creuzbauer's Battery, 5th Texas Artillery.  Every soldier in this battalion was born in Germany, and they all migrated to the U.S during the Civil War.  The second battalion was named Griffin’s Battalion, and was led by Col. William Henry Griffin.  The third battalion was Spaight’s Battalion, led by Lt. Col. Ashley W. Spaight.  And the final one was Daly’s Battalion, the only cavalry unit in the battle.  The U.S.S Wave and the U.S.S Granite City received orders to proceed to Calcasieu Pass.  When they arrived, immediately bombed an abandoned Confederate fort at the mouth of the river.  The Gunboats were sent with money to purchase cattle from local southern farmers.  The U.S.S Granite City ended up stealing cattle and horses from multiple farms.  This prompted a Confederate attack.  The local Confederate forces arrived quietly and prepared for a night-time attack on the Union forces.  When the Union went to sleep, they let less-experienced soldiers man the guns.  The Confederates seized the opportunity and moved their cannons closer.  The cannons lined up 1,000 yards away from the gunboats, while the cavalry and foot-soldiers advanced.  Numerous cannon shells penetrated the gunboat’s hulls.  While the cavalry and foot-soldiers moved in, the artillery advanced as well, and finished off the vessels.  On May 8th, Ella Morse, a Union Supply ship did not know of the Union casualties.  Then brought moved up all the way to the other ships with supplies.  When she noticed that confederates were manning the guns it was too late.  They gunned the ship down.  The Union Forces suffered many casualties.  They lost the Ella Morse, the U.S.S Granite City, the U.S.S Wave, and the U.S.S New London.  On the other hand, the Confederates did not lose too many soldiers.  The Confederates only suffered a few men from each battalion.

W. E. B. Griffin: William Edmund Butterworth III (born November 10, 1929), better known by his pen name W. E. B. Griffin, is a writer of military and detective fiction with 38 novels in six series published under that name.  He has also published under 11 other pseudonyms and three versions of his real name (W. E. Butterworth, William E. Butterworth, and most recently William E. Butterworth III).

Question: Which writer was born earliest, Mary Doria Russell or W. E. B. Griffin?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "earliest_born_writer": {
      "type": "string",
      "description": "The name of the writer who was born earliest."
    },
    "writers_compared": {
      "type": "array",
      "description": "Details of the writers whose birth dates were compared.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the writer."
          },
          "birth_year": {
            "type": "integer",
            "description": "The birth year of the writer."
          }
        },
        "required": [
          "name",
          "birth_year"
        ],
        "additionalProperties": false
      }
    },
    "comparison_result": {
      "type": "string",
      "description": "A statement summarizing the comparison of birth years."
    }
  },
  "required": [
    "earliest_born_writer",
    "writers_compared",
    "comparison_result"
  ],
  "additionalProperties": false
}
