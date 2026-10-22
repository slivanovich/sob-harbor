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
Fionn Carr: Fionn Carr (born 17 December 1985) is an Irish rugby union player.  He plays primarily as a wing but can also play at fullback.  Carr played most of his professional career for Irish province Connacht in the Pro12, and he holds the team record for most tries scored.  He also played for another Irish province, Leinster in the past.  Carr has represented Ireland at Schools, Under 19 and Under 21 level, as well as at international 'A' level and the Ireland national rugby sevens team.

Julie Feeney: Julie Feeney is an Irish singer, composer, songwriter and record producer who self-produces and self-orchestrates her own work.  She makes both instrumental and electronic music, and all of her songs with full orchestrations.  Feeney is a three-time nominee for the Meteor Choice Music Prize for 'Irish Album of the Year', winning in 2006 for debut album "13 songs".  She has released three studio albums on her own label 'mittens': "13 songs" (2005), "pages" (2009), and "Clocks" (2012).  "Clocks" entered at No.1 on the Irish Independent Albums Chart and No. 7 on the Main Irish albums charts making it her highest charting album to date.  She is from Galway, Ireland.  Previously she worked as a professional choral singer and educator.

Vince Feeney: Vincent Feeney (born 12 May 1973, Sligo), is a retired Irish professional boxer, nicknamed "the Sligo Kid", hailing from the Maugheraboy area of Sligo Town.  For the majority of his professional career, Feeney fought in the bantamweight division but also competed at divisions either side.

Little White Lie (TV drama): Little White Lie is a feature length IFTA-nominated Irish television romantic comedy drama broadcast on RTÉ One on 4 August 2008 at 21:30.  It stars Andrew Scott and Elaine Cassidy.  The drama follows the journey of a dejected actor (Scott) as he searches for love after being discarded by his highflying girlfriend.  The title comes from the fact that the main character tells one to his new girlfriend (Cassidy) - that he is a psychiatrist instead of an actor.  "Little White Lie" is written by Stuart Carolan and Barry Murphy and directed by Nick Renton.  It is produced by Element Pictures, which previously produced "Bitter Sweet" and "Prosperity" for RTÉ.  The drama featured music from the artist Julie Feeney.  The song "You Broke the Magic" was taken from the Choice Music Prize-winning "13 songs".

Adventures in Gramophone: Adventures in Gramophone is an album by the Northern Ireland based artist Duke Special.  It was released on Hag Records in 2005 and collects all twelve tracks from two previous EP releases - "Lucky Me" and "My Villain Heart".  It was nominated for the 2006 Choice Music Prize for Irish Album of the Year, losing out to "13 Songs" by Julie Feeney.

Leinster Rugby: Leinster Rugby (Irish: "Rugbaí Laighean" ) is one of the four professional provincial rugby teams from the island of Ireland and the most successful Irish team both domestically and in European competition.  They compete in the Pro14 and the European Rugby Champions Cup.  The team represents the Irish Rugby Football Union (IRFU) Leinster Branch, which is one of four primary branches of the IRFU and is responsible for rugby union throughout the geographical Irish province of Leinster.

Jim Feeney: James McBurney Feeney (23 June 1921 – March 1985) was a Northern Irish professional footballer.  During his career he made almost 100 appearances for Swansea City and over 200 appearances for Ipswich Town.  Feeney's son and grandson, both named Warren, later represented Northern Ireland.

Lord President of Munster: The post of Lord President of Munster was the most important office in the English government of the Irish province of Munster from its introduction in the Elizabethan era for a century, to 1672, a period including the Desmond Rebellions in Munster, the Nine Years' War, and the Irish Rebellion of 1641.  The Lord President was subject to the chief governor, but had full authority within the province, extending to civil, criminal and church legal matters, the imposition of martial law, official appointments, and command of military forces.  Some appointments to military governor of Munster were not accompanied by the status of President.  The width of his powers led to frequent clashes with the longer established courts, and in 1622 he was warned sharply not to "intermeddle" with cases which were properly the business of those courts.  He was assisted by a Council whose members included the Chief Justice of Munster, another justice and the Attorney General for the Province.  By 1620 his council was permanently based in Limerick.

Galway: Galway ( ; Irish: "Gaillimh" , ] ) is a city in the West of Ireland in the province of Connacht.  Galway City Council is the local authority for the city.  Galway lies on the River Corrib between Lough Corrib and Galway Bay and is surrounded by County Galway.  It is the fourth most populous urban area in the Republic of Ireland and the sixth most populous city in the island of Ireland.

Hanrahan: O'Hanrahan is an Irish surname shared by many Irish people and descendants of Irish emigrants.  The name is most common in the area of the Shannon Estuary (counties Kerry, Limerick and Clare) in Ireland.  Through emigration the name has become fairly common in the USA, the UK and other countries to which the Irish emigrated.  Many famous people share this name as well.  The name was originally spelled "Ó hAnnracháin" and initially used in the Irish province of Leinster, where local nobles and kings with the name ruled.  Variations include Hanradhan and Hanraghan.  Many families within Ireland and those of emigrants from Ireland, of the Ó hAnnracháin family, Anglicised their names to "O'Hanrahan" or "Hanrahan".  Eochaidh, King of Leinster, an early monarch who fled to Scotland in exile in 540, was the first ruler to bear the surname.  The name originates from Anradhán, diminutive of the Old Irish word "ánradh", which translates as "warrior".  The family motto is "An Uachtar" which means "The Champion".

Question: Which Irish province is Julie Feeney from?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person in question."
    },
    "origin_city": {
      "type": "string",
      "description": "The city where the person is from."
    },
    "irish_province": {
      "type": "string",
      "description": "The Irish province the city belongs to."
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation of how the province was determined from the city."
    }
  },
  "required": [
    "person_name",
    "origin_city",
    "irish_province",
    "reasoning"
  ],
  "additionalProperties": false
}
