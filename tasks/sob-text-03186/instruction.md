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
David-Louis Constant de Rebecque: David-Louis, Baron de Constant de Rebecque, seigneur d'Hermenches and Villars-Mendraz, a.k.a. David-Louis Constant d'Hermenches (17 November 1722 in Lausanne – 25 February 1785 in Paris) was a colonel and commandant of a Swiss regiment in the Dutch Republic and Maréchal de camp in French service with Swiss regiments.  He is also known for his contact with Voltaire and his correspondence with Isabelle de Charrière.

Baron de Blaquiere: Baron de Blaquiere, of Ardkill in the County of Londonderry, was a title in the Peerage of Ireland.  It was created in 1800 for the politician John Blaquiere, 1st Baron de Blaquiere, Chief Secretary for Ireland between 1772 and 1777.  He had already been created a Baronet, of Ardkill in the County of Londonderry, in the Baronetage of Ireland in 1784.  He was the son of Jean de Blaquiere, a merchant who emigrated to England from France in 1685.  Lord de Blaquiere was succeeded by his eldest son, the second Baron.  He died unmarried and was succeeded by his younger brother, the third Baron.  He was a general in the British Army.  His two sons, John the fourth Baron and William Barnard the fifth Baron, both succeeded in the title.  The latter was a Captain in the Royal Navy.  He was succeeded by his first cousin once removed, the sixth Baron.  He was the grandson of the Hon. Peter de Blaquière, fourth son of the first Baron.  Lord de Blaquiere's two sons were both killed in the First World War and on his death in 1920 the titles became extinct.

Baron de Freyne: Baron de Freyne, of Coolavin in the County of Sligo, is a title in the Peerage of the United Kingdom.  It was created in 1851 for Arthur French, 1st Baron de Freyne, with remainder to his younger brothers John, Charles and Fitzstephen French.  He had earlier represented County Roscommon in the House of Commons and later served as Lord Lieutenant of County Roscommon.  French had already been created Baron de Freyne, of Artagh in the County of Roscommon, in 1839, also in the Peerage of the United Kingdom but with normal remainder to heirs male.  Lord de Freyne was childless and on his death in 1856 the barony of 1839 creation became extinct.  The barony of 1851 creation survives according to the special remainder by his younger brother John, the second Baron.

Swiss Guards: Swiss Guards (French: "Gardes Suisses" ; German: "Schweizergarde" ) are the Swiss soldiers who have served as guards at foreign European courts since the late 15th century.

Marguerittes: Marguerittes is a commune in the Gard department in southern France.  In 1717, Antoine de Teissier (b.1667) was created the 1st Baron de Margeurittes.  One of his sons was a Huguenot who took refuge in Switzerland and his grandson, Jean Antoine de Teissier, 3rd Baron of Marguerittes, was guillotined 20 May 1794.  The 3rd Baron's son settled in England at Woodcote Park and was created Baron de Teissier by Louis XVIII in recognition of his father's sacrifices to France.

Pierre Victor, baron de Besenval de Brünstatt: Pierre Victor, baron de Besenval de Brünstatt (1722–1794) was the last commander of the Swiss Guards in France.

Armand de Camboust, duc de Coislin: Armand de Camboust, duc de Coislin (1 September 1635, Paris – 16 September 1702) was a French lieutenant général des armées du roi, and a duke and peer of France.  The son of a colonel in the Swiss Guards, he was elected a member of the Académie française in 1652 aged 16 and a half.  He died young and his seat was then held by his two sons, Pierre and Henri-Charles.

Captain D'Agoust: Captain D'Agoust was an officer of the Swiss Guards, described by Thomas Carlyle in his classic recounting of the French Revolution, as a "cast-iron" individual.  On 4 May 1788, fourteen months before the Revolution, the captain, acting on the order of the Court of Versailles, marched the Parliament of Paris out of the Palais de Justice and removed the key from the premises.  The event is considered one of the key mileposts on the road to the Revolution.

Concert Spirituel: The Concert Spirituel was one of the first public concert series in existence.  The concerts began in Paris in 1725 and ended in 1790; later, concerts or series of concerts of the same name occurred in Paris, Vienna, London and elsewhere.  The series was founded to provide entertainment during the Easter fortnight and on religious holidays when the other spectacles (the Paris Opera, Comédie-Française, and Comédie-Italienne) were closed.  The programs featured a mixture of sacred choral works and virtuosic instrumental pieces, and for many years took place in a magnificently-decorated Salle des Cent Suisses (Hall of the Hundred Swiss Guards) in the Tuileries Palace.  They started at six o’clock in the evening and were primarily attended by well-to-do bourgeois, the lower aristocracy, and foreign visitors.  In 1784 the concerts were moved to the stage area of the Salle des Machines (an enormous former opera house in the Tuileries), and in 1790, when the royal family was confined in the Tuileries, they took place in a Paris theater.

New Voyages to North America: New Voyages to North America is a book written by Louis Armand de Lom d’Arce, baron de Lahontan which chronicles the nine years Lahontan spent exploring New France as a soldier in the French Army.  The book, composed of two volumes, was published in 1703, originally in French as Nouveaux Voyages de Mr. le Baron de Lahontan dans l’Amérique Septentrionale.  An English edition was produced the same year.  The book is considered to be the best 17th century work on New France for its detailed descriptions of the environment as well as North American native society.  Lahontan’s work includes descriptions of the two winters he spent hunting with a group of the Algonquin people.  Lahontan expresses his opinions of New France and the natives as well as European society through his dialogue between himself and a fictional native, Adario, based on the Huron chief Kondiaronk.  Though fictional, this dialogue gives insight into his opinions of the native New France and Europe.  Both volumes provide valuable knowledge and information on the lands of New France from the perspective of a soldier in the French army as well as an explorer who explored the landscape, native peoples and developing economic, social, and political ties between the native peoples and French explorers.  The importance of the book is expressed by Gordon Sayre: “Lahontan takes a secular perspective throughout his writing which differentiates his works from those of the Jesuits that published during the same time he did”.  This book is an exploration narrative that tells an explorer's stories but also serves as a historical source for examining the American Indians in the New France region and the connections between the explorers and native peoples.

Question: Pierre Victor, baron de Besenval de Brünstatt (1722–1794) was the last commander of the Swiss Guards in France, Swiss Guards are the Swiss soldiers who have served as guards at foreign European courts since which late century?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "entity_name": {
      "type": "string",
      "description": "The name of the entity being described."
    },
    "role_description": {
      "type": "string",
      "description": "Description of the role or function of the entity."
    },
    "service_start_century": {
      "type": "integer",
      "description": "The century when the entity began its service."
    },
    "commander_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the commander."
        },
        "role": {
          "type": "string",
          "description": "The specific role of the commander within the entity."
        },
        "birth_year": {
          "type": "integer",
          "description": "The birth year of the commander."
        },
        "death_year": {
          "type": "integer",
          "description": "The death year of the commander."
        }
      },
      "required": [
        "name",
        "role",
        "birth_year",
        "death_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "entity_name",
    "role_description",
    "service_start_century",
    "commander_details"
  ],
  "additionalProperties": false
}
