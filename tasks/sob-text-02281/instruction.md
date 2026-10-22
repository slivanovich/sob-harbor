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
Cutthroat Kitchen: Cutthroat Kitchen is a cooking show hosted by Alton Brown that premiered on the Food Network on August 11, 2013.  It features four chefs competing in a three-round elimination cooking competition.  The contestants face auctions in which they can purchase opportunities to sabotage one another.  Each chef is given $25,000 at the start of the show; the person left standing keeps whatever money he/she has not spent in the auctions.  The show is in its fifteenth season as of November 2016.  The series shares some basic elements with other four-chef, three-round elimination-style competitions on Food Network including "Chopped" and "Guy's Grocery Games".  Numerous "Cutthroat Kitchen" contestants have competed on these shows.

Ciel, mon Pinard!: Ciel, mon Pinard!  was a very popular Quebec cooking show on Télé-Québec with Daniel Pinard as main chef and Josée Di Stasio as assistant.  While many kitchen shows tend to be formulaic, the success of this programme was in its offbeat, poetic digressions of the knowledgeable Pinard.  The show was a springboard for Di Stasio, who went off to star in her own cooking show, À la Di Stasio, after Pinard left the programme.  The title is a pun on the legendary line "Ciel, mon mari!"  ("Heavens, my husband!")  from the plays of French playwright Georges Feydeau.

Posh Nosh: Posh Nosh is a 2003 BBC television programme that parodies television chefs; the title and basic outline a reference to a cooking show pilot pitched by Neil Hamilton and Christine Hamilton.  Written by Jon Canter and Arabella Weir from an idea by Weir, and directed and script edited by Chris Langham, the programme stars Arabella Weir and Richard E. Grant as chefs the Hon. Simon and Minty Marchmont, owners of a very posh restaurant called the Quill & Tassel.  There were eight nine-minute episodes, in which the chefs carry out their mission to bring extraordinary food to ordinary people.

When Louis Met...: When Louis Met... is a series of documentary films by Louis Theroux.  The series was originally aired on BBC2 from 2000 to 2002.  In the series, Theroux accompanied a different British celebrity in each programme as they went about their day-to-day business, interviewing them about their lives and experiences as he did so.  His episode about Jimmy Savile "(When Louis Met... Jimmy)" was voted one of the top 50 documentaries of all time in a survey by Britain's Channel Four.  In another episode "("When Louis Met... the Hamiltons")", the Tory MP Neil Hamilton and his wife Christine were arrested during the course of filming following allegations of indecent assault which were subsequently found to be false.  The show did not return for a third series; Theroux said that he had difficulty in finding people to appear.

Trevor's World of Sport: Trevor's World of Sport began as a 2003 BBC television sitcom written and directed by Andy Hamilton and starring Neil Pearson as Trevor.  Only one television series was made, and Hamilton felt mistreated by the BBC over the scheduling of the show.  The first episode attracted an average of 3.4 million viewers, dropping to 2.9 million for the second and third episodes.  The subsequent episodes were rescheduled from Friday evenings (just after the 9:00pm watershed) to Monday nights (after the 10:00pm news), despite the Radio Times issues having already been published listing the originally scheduled transmission dates.  Hamilton went public with his displeasure over the show's scheduling and vowed never to work for BBC1 again, though he has since changed his mind.  A radio version was first broadcast on BBC Radio 4 in 2004, with subsequent series in 2005 and 2007.

Cooking with Master Chefs: Hosted by Julia Child: Cooking with Master Chefs was a PBS television cooking show that featured Julia Child visiting 16 celebrated chefs in the United States.  An episode that featured Lidia Bastianich was nominated for a 1994 Emmy Award.  Other chefs she visited included Emeril Lagasse, Jacques Pépin, and Alice Waters.  The show featured a companion book of the same name, published in 1993 (ISBN  ).  Reruns of the show currently air on WUCF-TV.

Iron Chef: Iron Chef (料理の鉄人 , Ryōri no Tetsujin , literally "Ironmen of Cooking") is a Japanese television cooking show produced by Fuji Television.  The series, which premiered on October 10, 1993, is a stylized cook-off featuring guest chefs challenging one of the show's resident "Iron Chefs" in a timed cooking battle built around a specific theme ingredient.  The series ended on September 24, 1999, although occasional specials were produced until 2002.  The series aired 309 episodes.  Repeats are regularly aired on the Food Network in Canada, the Cooking Channel in the United States and on Special Broadcasting Service in Australia.  Fuji TV aired a new version of the show, titled Iron Chef (アイアンシェフ , Aian Shefu ) , starting on October 26, 2012.

MasterChef: The Professionals: MasterChef: The Professionals is a BBC television competitive cooking show aired on BBC Two.  It is a spin-off from the main "MasterChef" series, for professional working chefs.  Introduced in 2008, Gregg Wallace and India Fisher reprised their roles as co-judge and voiceover respectively.  "MasterChef" judge John Torode was replaced by Michel Roux Jr., a two-Michelin-star chef, assisted, from 2009, by his sous-chef Monica Galetti.  Since 2011, Sean Pertwee has taken over Fisher's role as voiceover.

Emel Başdoğan: Emel Başdoğan (born 26 March 1960) is a Turkish celebrity chef, author of cooking and baking books, and media personality known for her television shows and publications.  She was a judge on the television programme Ver Fırına, the Turkish version of the Great British Bake Off for 170 episodes.

Christine Hamilton: Mary Christine Hamilton (née Holman; born 10 November 1949) is an English media personality and author.  She is married to Neil Hamilton, the former Conservative Member of Parliament for Tatton,

Question: Posh Nosh is a 2003 BBC television programme that parodies television chefs; the title and basic outline a reference to a cooking show pilot pitched by Neil Hamilton and Mary Christine Hamilton, an English media personality and author, born on which date?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "program_name": {
      "type": "string",
      "description": "The name of the television program being discussed."
    },
    "program_type": {
      "type": "string",
      "description": "The type of the program, e.g., 'parody television programme'."
    },
    "referenced_individuals": {
      "type": "array",
      "description": "A list of individuals whose work or persona is referenced by the program.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The full name of the individual."
          },
          "role_in_reference": {
            "type": "string",
            "description": "How the individual is involved in the reference, e.g., 'pitched cooking show pilot'."
          },
          "description": {
            "type": "string",
            "description": "A brief description of the individual, if available."
          },
          "birth_date": {
            "type": "string",
            "description": "The birth date of the individual, if available."
          }
        },
        "required": [
          "name",
          "role_in_reference"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "program_name",
    "program_type",
    "referenced_individuals"
  ],
  "additionalProperties": false
}
