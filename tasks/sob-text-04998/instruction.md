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
Free, prior and informed consent: The aim of Free Prior Informed consent (FPIC), is to establish bottom up participation and consultation of an Indigenous Population prior to the beginning of a development on ancestral land or using resources within the Indigenous Population's territory.  Indigenous people (IP) have a special connection to their land and resources, they inhabit 20% of the earth's surface, these areas are environmentally rich in both renewable and non-renewable resources.  The collective ownership style of most Indigenous Peoples conflicts with the modern global market and its continuous need for resources and land.  To protect Indigenous peoples rights, international human rights law has created process and standards to safeguard their way of life and to encourage participation in the decision making process.  One of these methods is the process of FPIC.

Intercultural Universities in Mexico: Intercultural Universities in Mexico are higher education institutions which were established in 2004 in response to the lack of enrollment of the indigenous population in Mexico.  While an estimated 10% of the population of Mexico is indigenous, it is the least represented in higher education.  According to estimates, only between 1% and 3% of higher education enrollment in Mexico is indigenous.  In response to this inequality, the General Coordination for Intercultural and Bilingual Education at the Ministry of Education established Intercultural Universities with the active participation of indigenous organizations and academic institutions in each region.  These institutions are located in densely indigenous areas and, though they allow for diversity in enrollment, they are especially intended for the indigenous population.  Founded on the principle of intercultural education, they aim to foster dialogue between different cultures and represent a way of responding to both the historical and more recent demands of indigenous peoples.

Passion for Skiing: Passion for Skiing is a book published in 2010 about the contributions of people from Hanover, New Hampshire and Dartmouth College to winter activities, particularly the sport of downhill skiing and highlights this history of skiing from 1910 to the current era.  It was authored by Dartmouth alumnus Stephen L. Waterhouse (Dartmouth College Class of 1965, Tuck Business School Class of 1967), a native of Sanford Maine and part-time Vail, Colorado resident with the help of other alumni and ski historians.

Pomier Caves: The Pomier Caves are a series of 55 caves located north of San Cristobal in the south of the Dominican Republic.  They contain the largest collection of rock art in the Caribbean created since 2,000 years ago primarily by the Taíno people but also the Carib people and the Igneri, the pre-Columbian indigenous inhabitants of the Bahamas, Greater Antilles, and some of the Lesser Antilles.  These caves have been damaged by the uncontrolled mining of limestone nearby.

Aaron Carapella: Aaron Carapella is a self-taught cartographer who makes maps of the locations and names of Pre-Columbian Indigenous tribes of North America circa 1490.  He is part Cherokee on his mother's side and his grandparents instilled a deep interest in Native American culture.  At age 19, he began his map-making research and as of 2014, he has made maps of indigenous tribes with their original names for the continental United States, Canada, and Mexico.

Calamari people: The Calamari people are a pre-Columbian indigenous ethnic group of the area that is now Cartagena, Colombia.  It is related to the Puerto Hormiga archaeological site

Nage: The Nage are an indigenous people living on the eastern Indonesian island of Flores and Timor.  They descended from the indigenous population of Flores They are largely assimilated by the neighboring people.  They speak Nage language, one of the major languages in the Austronesian languages group.

Eleazar Wheelock: Eleazar Wheelock (April 22, 1711 – April 24, 1779) was an American Congregational minister, orator, and educator in Lebanon, Connecticut, for 35 years before founding Dartmouth College in New Hampshire.  He had tutored Samson Occom, a Mohegan who became a Presbyterian minister and the first Native American to publish writings in English.  Before founding Dartmouth, Wheelock had founded and run the Moor's Charity School in Connecticut to educate Native Americans.  The college was primarily for the sons of English colonists.

Native Americans in the United States: In the United States of America, Native Americans (also known as American Indians, Indigenous Americans or simply Indians; see §Terminology differences) are people who belong to one of the over 500 distinct Native American tribes that survive intact today as partially sovereign nations within the country's modern boundaries.  These tribes and bands are descended from the pre-Columbian indigenous population of North America.

Dartmouth College: Dartmouth College ( ) is a private Ivy League research university in Hanover, New Hampshire, United States.  Established in 1769 by Eleazar Wheelock, it is the ninth-oldest institution of higher education in the United States and one of the nine colonial colleges chartered before the American Revolution.  Although founded as a school to educate Native Americans in Christian theology and the English way of life, Dartmouth primarily trained Congregationalist ministers throughout its early history before it gradually secularized, emerging at the turn of the 20th century from relative obscurity into national prominence.

Question: Dartmouth College was founded to educate which group of people descended from the pre-Columbian indigenous population of North America?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "college_name": {
      "type": "string",
      "description": "The name of the educational institution."
    },
    "founding_year": {
      "type": "integer",
      "description": "The year the institution was established."
    },
    "primary_educational_target": {
      "type": "object",
      "properties": {
        "group_name": {
          "type": "string",
          "description": "The name of the primary group the institution was founded to educate."
        },
        "group_origin_description": {
          "type": "string",
          "description": "A description of the origin of the target group, linking them to pre-Columbian indigenous populations."
        },
        "educational_focus": {
          "type": "string",
          "description": "The specific areas of education intended for the target group."
        }
      },
      "required": [
        "group_name",
        "group_origin_description",
        "educational_focus"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "college_name",
    "founding_year",
    "primary_educational_target"
  ],
  "additionalProperties": false
}
