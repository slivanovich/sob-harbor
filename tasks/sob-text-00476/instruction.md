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
In Search for Captain Grant: In Search for Captain Grant (Russian: В поисках капитана Гранта , "V poiskakh kapitana Granta " , Bulgarian: По следите на капитан Грант ) is a 1986 Soviet 7-part television miniseries adaptation of Jules Verne's novel "In Search of the Castaways" directed by Stanislav Govorukhin.  It was shot on the Odessa Film Studio and Bulgarian Boyana Film in 1985.

Barbara Hicks: Barbara Hicks (12 August 1924 – 6 September 2013) was an English film actress.  She appeared in Terry Gilliam's 1985 cult film "Brazil" and Merchant Ivory Productions's 1992 Bafta award-winning "Howards End".

Over Here (miniseries): Over Here is a 2-part television miniseries made in 1996 by the BBC for BBC1 from 7 to 8 April 1996, this comedy-drama miniseries chronicling the lives of US Army Air Corps B-17 Flying Fortress bomber crews on a Royal Air Force Spitfire base during World War II.  Samuel West starred as the RAF pilot Archie Bunting.

Luciana Arrighi: Luciana Maria Arrighi {'1': ", '2': ", '3': ", '4': "} (born 1940) is a Brazilian-born, Australian-raised, Italian production designer.  She won an Academy Award for the film "Howards End" in the category Best Art Direction.

Holocaust (miniseries): Holocaust is a 1978 American four part television miniseries which tells the story of the Holocaust from the perspective of the (fictional) Weiss family of German Jews and that of a rising member of the SS, who gradually becomes a merciless war criminal.  "Holocaust" highlighted numerous important events which occurred up to and during World War II, such as "Kristallnacht", the creation of Jewish ghettos and later, the use of gas chambers.  Although the miniseries won several awards and received critical acclaim, it was criticized by some, including noted Holocaust survivor and author Elie Wiesel, who described it as "untrue and offensive."

Vanessa Redgrave filmography: The following is the filmography of actress Vanessa Redgrave.  She has appeared in numerous films and television series and has received six Academy Award nominations, for "Morgan: A Suitable Case for Treatment" (1966), "Isadora" (1968), "Mary, Queen of Scots" (1971), "Julia" (1977), "The Bostonians" (1984) and "Howards End" (1992).  She appeared in the 2013 film "The Butler" as Annabeth Westfall.

Howards End (miniseries): Howards End is an upcoming television miniseries directed by Hettie MacDonald.  It is based on the 1910 novel of the same name by E. M. Forster and adapted by Kenneth Lonergan.  It will air on BBC One in the United Kingdom and on Starz in the United States.  The series will consist of four episodes.

Samuel West: Samuel Alexander Joseph West, also known as Sam West (born 19 June 1966), is an English actor and director.  He is best known for his role in the film "Howards End" and his work on stage (including the award-winning play "Enron").

The Crimson Petal and the White (miniseries): The Crimson Petal and the White is a 2011 four part television miniseries, adapted from Michel Faber's 2002 novel "The Crimson Petal and the White".  Starring Romola Garai as Sugar and Chris O'Dowd as William Rackham, the miniseries aired in the UK during April 2011 on BBC Two.  The supporting cast includes Shirley Henderson, Richard E. Grant and Gillian Anderson.  Critical reviews of the miniseries were mixed but generally positive.

Joseph Quinn (actor): Joseph Quinn is a British actor.  He is known for his role as Arthur Havisham in the television series "Dickensian", and for his upcoming role in the miniseries "Howards End".

Question: Which role does this English actor and director, who appeared in the film "Howards End," play on the 2-part television miniseries "Over Here?"

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the actor."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the actor."
        },
        "profession": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "The professions of the actor."
        }
      },
      "required": [
        "name",
        "nationality",
        "profession"
      ],
      "additionalProperties": false
    },
    "miniseries": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the miniseries."
        },
        "number_of_parts": {
          "type": "integer",
          "description": "The number of parts in the miniseries."
        }
      },
      "required": [
        "title",
        "number_of_parts"
      ],
      "additionalProperties": false
    },
    "role_played": {
      "type": "object",
      "properties": {
        "character_name": {
          "type": "string",
          "description": "The name of the character played."
        },
        "role_description": {
          "type": "string",
          "description": "A description of the character's role."
        }
      },
      "required": [
        "character_name",
        "role_description"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "actor",
    "miniseries",
    "role_played"
  ],
  "additionalProperties": false
}
