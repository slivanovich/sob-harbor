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
List of incidents of civil unrest in France: This is a list of incidents of civil unrest in France.  Civil unrest can include, rioting, strikes, violent labor disputes, or minor insurrections.

Portland Rum Riot: The Portland Rum Riot, also called the Maine Law Riot, was a brief but violent period of civil unrest that occurred in Portland, Maine on June 2, 1855, in response to the Maine law which prohibited the sale and manufacture of alcohol in the state from 1851.

Neal Dow: Neal Dow (March 20, 1804 – October 2, 1897) was an American Prohibition advocate and politician.  Nicknamed the "Napoleon of Temperance" and the "Father of Prohibition", Dow was born to a Quaker family in Portland, Maine.  From a young age, he believed alcohol to be the cause of many of society's problems and sought to ban it through legislation.  In 1850, Dow was elected president of the Maine Temperance Union, and the next year he was elected mayor of Portland.  Soon after, largely due to Dow's efforts, the state legislature banned the sale and production of alcohol in what became known as the Maine law.  Serving twice as mayor of Portland, Dow enforced the law with vigor and called for increasingly harsh penalties for violators.  In 1855, his opponents rioted and he ordered the state militia to fire on the crowd.  One man was killed and several wounded, and when public reaction to the violence turned against Dow, he chose not to seek reelection.

Neal Dow House: The Neal Dow House, also known as Gen. Neal Dow House, is an historic house found at 714 Congress Street in Portland, Maine.  It was built in 1829 for noted politician and prohibitionist Neal Dow (1804-1897), and was later designated a National Historic Landmark for that association.  Dow was the author of the first prohibition law passed by the Maine legislature in 1851 (and giving such laws the epithet "Maine law").  He was known as a tireless, internationally known activist for the temperance movement.  Dow's house was a center of activism in his lifetime, and is now the headquarters of the Maine chapter of the Women's Christian Temperance Union.

Edward C. Delavan: Edward Cornelius Delavan (1793–1871) was a wealthy businessman who devoted much of his fortune to promoting the temperance movement.  He helped establish the American Temperance Union; attacked the use of wine in Christian communion; established a temperance hotel in Albany, New York; traveled to Europe to promote teetotalism.  He helped spearhead the local option movement in New York during the 1840s by which local majorities could vote their towns dry.  In 1846, he received the nomination for the Governorship of New York from the Native American Party, but he declined it.  He was also active in the Maine Law prohibition movement of the 1850s.  He later sent a copy of a temperance tract to every soldier in the Union Army during the Civil War (a million copies in all); and sponsored a series of periodicals.  They included the "Journal of the American Temperance Union", the "Temperance Recorder", the "American Temperance Intelligencer"; the "Enquirer", and the "Prohibitionist".  Prohibition or dry towns in Illinois and Wisconsin were named in his honor.

William E. Johnson: William Eugene "Pussyfoot" Johnson (25 March 1862 – 2 February 1945) was an American Prohibition advocate and law enforcement officer.  In pursuit of his campaign to outlaw intoxicating beverages, he went undercover, posing as an habitué of saloons and collecting information against their owners.  He gained the nickname "Pussyfoot" due to his cat-like stealth in the pursuit of suspects in the Oklahoma Territory.

American Prohibition Foundation: The American Prohibition Foundation is a Colorado corporation created in 2002 by a faction of the Prohibition Party headed by Earl Dodge.  It is not associated with the National Prohibition Foundation which was originally incorporated in Indiana in 1952.  Both foundations exist to promote the work of the temperance movement and prohibition.

2005 Maldives civil unrest: The 2005 Maldivian civil unrest refers to the civil unrest that broke out in Malé, Gaafu Dhaalu Atoll and Addu Atoll of the Maldives on August 12, 2005 which led to events that supported the democratic reform of the country.  This unrest was provoked by the arrest of Mohamed Nasheed - an open critic of the president Maumoon Abdul Gayoom - and the subsequent demolition of the "Dhunfini tent", used by the members of the Maldivian Democratic Party (MDP) for their gatherings.  Supporters of MDP were quick to demonstrate.  They started calling for the resignation of Maumoon Abdul Gayoom, soon after Nasheed's arrest.  Several arrests were made on the first night followed by the demolition of the Dhunfini tent.  The demolition complicated the situation further provoking the unrest.  The unrest grew violent on the third night, on August 14, 2005, due to the methods used in the attempts by the authority to stop the demonstration.

List of riots and civil unrest in Calgary: The following is a timeline of riots and civil unrest in Calgary, Alberta.  Since its incorporation as a town in 1884, like other cities, Calgary has had to deal with a variety of violence.  Calgary has been credited with maintaining relative civility during duress.  The Great Depression in Canada has received particular attention from sociologists and historians, including Thomas Thorner and Neil Watson who wrote, "There is little question that Calgary experienced its share of civil strife during the Depression.  Battles between police and the single unemployed men, full scale riots and threats to blow up public buildings appear to have been almost annual events."  According to Stephen Graham, a Professor of Human Geography at Durham University, recent events have seen the City of Calgary change their tactics towards civil unrest activities such as protests.

1992 Los Angeles riots: The 1992 Los Angeles riots, also known as the Rodney King riots, the South Central riots, the 1992 Los Angeles civil disturbance, the 1992 Los Angeles civil unrest, and the Los Angeles uprising, were a series of riots, lootings, arsons, and civil disturbances that occurred in Los Angeles County, California in April and May 1992.  The unrest began in South Central Los Angeles on April 29 after a trial jury acquitted four officers of the Los Angeles Police Department of the use of excessive force in the videotaped arrest and beating of Rodney King.  It then spread throughout the Los Angeles metropolitan area as thousands of people rioted over a six-day period following the announcement of the verdict.

Question: What was a brief but violent period of civil unrest in response to the Maine law, who's opponents of an American Prohibition advocate and politician Nicknamed the "Napoleon of Temperance" rioted ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "unrest_event": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the civil unrest event."
        },
        "description": {
          "type": "string",
          "description": "A brief description of the nature of the unrest."
        },
        "date": {
          "type": "string",
          "description": "The date when the civil unrest occurred."
        }
      },
      "required": [
        "name",
        "description",
        "date"
      ],
      "additionalProperties": false
    },
    "triggering_legislation": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the law that triggered the unrest."
        },
        "purpose": {
          "type": "string",
          "description": "The main purpose or effect of the legislation."
        }
      },
      "required": [
        "name",
        "purpose"
      ],
      "additionalProperties": false
    },
    "key_figure_involved": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the key political figure whose opponents rioted."
        },
        "role": {
          "type": "string",
          "description": "The role or profession of the key figure."
        },
        "nickname": {
          "type": "string",
          "description": "A notable nickname of the key figure."
        },
        "opponents_action": {
          "type": "string",
          "description": "The action taken by the opponents of the key figure."
        }
      },
      "required": [
        "name",
        "role",
        "nickname",
        "opponents_action"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "unrest_event",
    "triggering_legislation",
    "key_figure_involved"
  ],
  "additionalProperties": false
}
