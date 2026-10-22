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
Arnold Janssen: Saint Arnold Janssen, S.V.D. (5 November 1837 – 15 January 1909), was a German-Dutch Roman Catholic priest and missionary who is venerated as a saint.  He founded the Society of the Divine Word, a Roman Catholic missionary religious congregation, also known as the "Divine Word Missionaries", as well as two congregations for women.  In 1889 he founded in Steyl, Netherlands, the Missionary Sisters Servants of the Holy Spirit and in 1896 at the same place the Holy Spirit Adoration Sisters.  He was canonized on 5 October 2003, by Pope John Paul II.

Missionary Society of St Paul (Malta): The Missionary Society of St. Paul (Maltese: "Soċjeta' Missjunarja ta' San Pawl" , MSSP) is a Roman Catholic missionary congregation of priests and brothers, founded in Malta in 1910 by Mgr.  Joseph De Piro.  According to its Constitutions, "the purpose of the Society is the evangelisation and the implanting of the Church in missionary lands known as mission "Ad Gentes".  Consequently its apostolic endeavours in those countries not strictly considered missionary must be orientated towards promoting and creating an awareness of missionary activity."

Jerome Cabeen: Jerome Cabeen (born July 18, 1967) is an author, speaker, social justice advocate and missionary originally from Houston, Texas (US).  He is the author of Amazon.com bestseller, "Memoirs of a Reluctant Servant –Two Years of Triumph and Sorrow in Liberia, Africa".  The book reached #1 on the Amazon.com Bestseller List in the Coastal West Africa category.  Cabeen lived in Honduras, Central America, from 2004 to 2008 and Liberia, West Africa, from 2008 to 2010, volunteering as a missionary for Franciscan Works, a Catholic missionary organization in Chicago, Illinois.  Currently he resides in Beaumont, Texas and works for the Catholic Diocese of Beaumont.  He is a practicing Catholic and travels around the United States giving talks and lectures on Liberia, Honduras, social justice teachings and missionary work.

Potawatomi: The Pottawatomi , also spelled Pottawatomie and Potawatomi (among many variations), are a Native American people of the Great Plains, upper Mississippi River and Western Great Lakes region.  They traditionally speak the Potawatomi language, a member of the Algonquian family.  The Potawatomi called themselves Neshnabé, a cognate of the word "Anishinaabe".  The Potawatomi were part of a long-term alliance, called the Council of Three Fires, with the Ojibwe and Odawa (Ottawa).  In the Council of Three Fires, the Potawatomi were considered the "youngest brother" and were referred to in this context as Bodéwadmi, a name that means "keepers of the fire" and refers to the council fire of three peoples.

Benjamin Petit: Benjamin Marie Petit (April 8, 1811 – February 10, 1839) was a Catholic missionary to the Potawatomi at Twin Lakes, Indiana,

Pontifical Missionary Union: The Pontifical Missionary Union (PMU) is a Catholic missionary society founded by blessed Paolo Manna in 1916, a missionary who served in Myanmar.  Its aim is to increase awareness of the Church's worldwide mission among people engaged in pastoral ministry.  It is one of four Pontifical Mission Societies of the Roman Catholic Church.

Apostolic Missionary Union: The Apostolic Missionary Union also known as Apostolic Missionary House and the Catholic Missionary Union and was an organisation run by the Catholic Bishops of the United States to further missionary activity in the United States.  It was strongly influenced by the Paulist Fathers.

Rosary Convent High School: Rosary Convent High School is a Roman Catholic missionary private-run girls' school in Hyderabad, India.  Established in 1904 by the Franciscan Missionaries of Mary, it continues to be run by these Missionary Sisters who reside in their convent at the school's grounds.  The school was established in response to a need for Catholic girls' education.  It became the sister school to All Saints High School, the area's prime Catholic boys' school in those days.  These two schools are located on either side of St Joseph's Cathedral in Gunfoundry, Hyderabad, India.

Missionary Society of Saint Thomas: The Missionary Society of St Thomas the Apostle is a Catholic missionary organization founded in 1968 in Kerala by the Syro Malabar Church, for missionary work in "less Christian areas" in and outside India.  It was founded by bishop Sebastian Vayalil as a Society of Apostolic Life.

Pavlin Demski: Pavlin Demski or Paulin Demski was a 17th-century Catholic missionary whose activities were aimed to convert Orthodox Serbs to Catholicism.  In the middle of the 17th century he was the main Catholic missionary in Montenegro.  Demski was suitable person for propagation of the Eastern Catholicism also because he was from the territory whose people were already converted, so this conversion could be used as an example.

Question: Who was a Catholic missionary to the group of people who called themselves Neshnabé?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "missionary_name": {
      "type": "string",
      "description": "The full name of the Catholic missionary."
    },
    "missionary_role": {
      "type": "string",
      "description": "The primary role or title of the missionary."
    },
    "group_name": {
      "type": "string",
      "description": "The common name of the indigenous group the missionary served."
    },
    "group_self_designation": {
      "type": "string",
      "description": "The name the indigenous group used to refer to themselves."
    },
    "group_language_family": {
      "type": "string",
      "description": "The language family to which the group's traditional language belongs."
    },
    "group_primary_region": {
      "type": "string",
      "description": "The primary geographical region associated with the indigenous group."
    }
  },
  "required": [
    "missionary_name",
    "missionary_role",
    "group_name",
    "group_self_designation",
    "group_language_family",
    "group_primary_region"
  ],
  "additionalProperties": false
}
