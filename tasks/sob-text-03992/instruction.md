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
Judaism: Judaism (originally from Hebrew , "Yehudah", "Judah"; via Latin and Greek) is an ancient monotheistic Abrahamic religion with the Torah as its foundational text.  It encompasses the religion, philosophy and culture of the Jewish people.  Judaism is considered by religious Jews to be the expression of the covenant that God established with the Children of Israel.  Judaism includes a wide corpus of texts, practices, theological positions, and forms of organization.  The Torah is part of the larger text known as the Tanakh or the Hebrew Bible, and supplemental oral tradition represented by later texts such as the Midrash and the Talmud.  With between 14.5 and 17.4 million adherents worldwide, Judaism is the tenth-largest religion in the world.

World Union for Progressive Judaism: The World Union for Progressive Judaism (WUPJ) is the international umbrella organization for the various branches of Reform, Liberal and Progressive Judaism, as well as the separate Reconstructionist Judaism.  The WUPJ is based in 40 countries with 1,275 affiliated synagogues, of which 1,170 are Reform, Progressive or Liberal and 105 Reconstructionist.  It claims to represent a total of some 1.8 million people, both registered constituents and non-member identifiers.  The WUPJ states that it aims are to create common ground between its constituents and to promote Progressive Judaism in places where individuals and groups are seeking authentic, yet modern ways of expressing themselves as Jews.  It seeks to preserve Jewish integrity wherever Jews live, to encourage integration without assimilation, to deal with modernity while preserving the Jewish experience and to strive for equal rights and social justice.

Society for the Advancement of Judaism: The Society for the Advancement of Judaism is a synagogue and Jewish organization in New York City, on Manhattan's Upper West Side.  Founded in 1922 by Rabbi Mordecai M. Kaplan, the founder of Reconstructionist Judaism, the synagogue is affiliated with the Reconstructionist Jewish movement.

African-American Jews: African-American Jews are people of mixed Jewish-African-American background or African Americans who are both born Jewish and who have converted to Judaism.

Karaite Jewish University: The Karaite Jewish University is a non-profit corporation incorporated in California, U.S.A., in November 2005 for the purposes of disseminating the study of Karaite Judaism.  Karaite Jewish University is not accredited as an academic institution.  However, it has been authorized by the Council of Sages of Universal Karaite Judaism to teach an Introduction to Karaite Judaism course, both for Rabbinic Jews wishing to affiliate formally with Karaite Judaism, as well as potential converts to Judaism according to Karaite practice.  Universal Karaite Judaism is the official body recognized by the State of Israel as representing Karaite Jews in matters of personal status.  The university's first “Introduction to Judaism” class began in February 2006 and ended in May 2007.  Ten of the graduates from the course converted to Judaism together with their children under the auspices of Congregation Bnai Israel of the Karaite Jews of America in Daly City, California, on July 30, 2007.  These were the first official sanctioned conversions to Judaism according to the Karaite rite since 1465.  On September 2, 2007, the university awarded an Honorary Doctorate degree in Education to Mourad El-Kodsi, historian and author of The Karaite Jews of Egypt and The Karaites of Poland, Lithuania, Russia & Ukraine.  El-Kodsi was named Dean Emeritus of the university whose function will be to mentor the university's graduate students.

Same-sex marriage and Judaism: Same-sex marriage in Judaism has been a subject of debate within Jewish denominations.  The traditional view among Jews is to regard same-sex relationships as categorically forbidden by the Torah.  This remains the current view of Orthodox Judaism, but not of Reconstructionist Judaism, Reform Judaism and Conservative Judaism, which started changing its position to same-sex unions in 2006.

Shimsat Nuthar: Shimsat Nuthar is a reconstructionist religion.  It is a very small but growing faith tradition experiencing revival among African Americans.  The church advertises itself as the religion of "The Black Nation".

American Jews: American Jews, or Jewish Americans, are Americans who are Jews, whether by religion, ethnicity or nationality.  The current Jewish community in the United States consists primarily of Ashkenazi Jews, who comprise about 90% of the American Jewish population.  Most American Ashkenazim are US-born, with a dwindling number of now elderly earlier immigrants, as well as some more recent foreign-born immigrants.  During the colonial era, prior to the mass immigration of Ashkenazim, Spanish and Portuguese Jews represented the bulk of America's then small Jewish population, and while their descendants are a minority today, they along with an array of other Jewish communities represented the remainder of American Jews, including other more recent Sephardic Jews, Mizrahi Jews, various other ethnically Jewish communities, as well as a smaller number of converts to Judaism.  The American Jewish community manifests a wide range of Jewish cultural traditions, encompassing the full spectrum of Jewish religious observance.

Reconstructionist Rabbinical Association: The Reconstructionist Rabbinical Association (RRA) founded in 1974, is the professional association of rabbis affiliated with Reconstructionist Judaism.  It has approximately 300 members, most of whom are graduates of the Reconstructionist Rabbinical College in Wyncote, Pennsylvania, near Philadelphia.  The association is a member of a number of national coalitions including the Conference of Presidents of Major American Jewish Organizations.

Alliance of Black Jews: The Alliance of Black Jews was an American organization that was started in Chicago, Illinois, in 1995 by a group of African Americans who self-identified as Jews and Black Hebrews.  At the time, they estimated that there were about 200,000 black Jews in the United States.  The figure, which included Black Hebrew Israelites (not recognized as Jews by mainstream Judaism), as well as Reform, Conservative, Orthodox and Reconstructionist African-American Jews by birth or conversion, was based in part on the 1990 Jewish Population Study, which gave figures ranging from 135,000 to 260,000, depending on the definition of a Jew.

Question: The Alliance of Black Jews was an American organization that included, which Reconstructionist religion, that are people of mixed Jewish-African-American background, or African Americans who are both born Jewish and who have converted to Judaism?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "organization_name": {
      "type": "string",
      "description": "The name of the organization mentioned in the question."
    },
    "included_groups": {
      "type": "array",
      "description": "A list of types of Jewish groups included in the organization.",
      "items": {
        "type": "string"
      }
    },
    "reconstructionist_group_identified": {
      "type": "string",
      "description": "The specific Reconstructionist group that matches the description provided in the question."
    },
    "group_description": {
      "type": "string",
      "description": "The definition or description of the identified group as per the context."
    }
  },
  "required": [
    "organization_name",
    "included_groups",
    "reconstructionist_group_identified",
    "group_description"
  ],
  "additionalProperties": false
}
