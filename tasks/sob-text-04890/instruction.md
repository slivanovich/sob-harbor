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
Welsh Springer Spaniel: The Welsh Springer Spaniel is a breed of dog and a member of the spaniel family.  Thought to be comparable to the old Land Spaniel, they are similar to the English Springer Spaniel and historically have been referred to as both the Welsh Spaniel and the Welsh Cocker Spaniel.  They were relatively unknown until a succession of victories in dog trials by the breed increased its popularity.  Following recognition by The Kennel Club in 1902, the breed gained the modern name of Welsh Springer Spaniel.  The breed's coat only comes in a single colour combination of white with red markings, usually in a piebald pattern.  Loyal and affectionate, they can become very attached to family members and are wary of strangers.  Health conditions are limited to those common among many breeds of dog, although they are affected more than average by hip dysplasia and some eye conditions.  They are a working dog, bred for hunting, and while not as rare as some varieties of spaniel, they are rarer than the more widely known English Springer Spaniel with which they are sometimes confused.

Mississippi Hound Dogs: The Mississippi Hound Dogs were a professional indoor football team based in Tupelo, Mississippi.  The Hound Dogs played their home games at the BancorpSouth Arena as a member of the Ultimate Indoor Football League's Southern Conference.

Russian Spaniel: The Russian Spaniel is a type of spaniel first standardised in 1951 in the Soviet Union after World War II by cross breeding English Cocker Spaniels, English Springer Spaniels and other spaniel breeds.  Physically it is similar to a Cocker Spaniel, but has a shorter, tighter coat and a longer body.  Developed and used as hunting dogs, this breed does not suffer from any major health complaints other than those normally associated with spaniels.  Popular in its native Russia, the breed was only introduced overseas in the 1990s, and is not yet recognised by any major kennel clubs.

Norfolk Spaniel: The Norfolk Spaniel or Shropshire Spaniel is an extinct breed of dog since the early 20th century.  It was originally thought to have originated from the work of one of the Dukes of Norfolk, but this theory was disproven after being in doubt during the later part of the 19th century.  The term was used to designate springer type spaniels that were neither Sussex nor Clumber Spaniels, and attempts were made to use it to specify a breed that would later become known as the English Springer Spaniel.

English Springer Spaniel: The English Springer Spaniel is a breed of gun dog in the Spaniel family traditionally used for flushing and retrieving game.  It is an affectionate, excitable breed with a typical lifespan of twelve to fourteen years.  They are very similar to the Welsh Springer Spaniel and are descended from the Norfolk or Shropshire Spaniels of the mid-19th century; the breed has diverged into separate show and working lines.  The breed suffers from average health complaints.  The show-bred version of the breed has been linked to "rage syndrome", although the disorder is very rare.  It is closely related to the Welsh Springer Spaniel and very closely to the English Cocker Spaniel; less than a century ago, springers and cockers would come from the same litter.  The smaller "cockers" hunted woodcock while the larger littermates were used to flush, or "spring," game.  In 1902, The Kennel Club recognized the English Springer Spaniel as a distinct breed.  They are used as sniffer dogs on a widespread basis.  The term "Springer" comes from the historic hunting role, where the dog would flush (spring) birds into the air.

Felicity's Diamond Jim: Ch.  Felicity's Diamond Jim, CD, RE (June 8, 2000 – May 6, 2011), commonly known as James, was an English Springer Spaniel, best known for being the 2007 Best In Show winner at the Westminster Dog Show.  It was his 51st Best in Show victory, and his last, as his owners chose to retire James after the win to focus him on his work as a certified therapy dog.  He was handled exclusively by the same handler who took Ch.  Salilyn 'N Erin's Shameless to a best-in-show at Westminster in 2000.  In retirement he was recognised in 2008 by the English Springer Spaniel Field Trial Association for his work as a sire and has produced many champion offspring, including Ch.  Cerise Jesse James.

English Cocker Spaniel: The English Cocker Spaniel is a breed of gun dog.  The English Cocker Spaniel is an active, good-natured, sporting dog standing well up at the withers and compactly built.  There are "field" or "working" cockers and "show" cockers.  It is one of several varieties of spaniel and somewhat resembles its American cousin, the American Cocker Spaniel, although it is closer to the working-dog form of the Field Spaniel and the English Springer Spaniel.

Springer Spaniel: Springer Spaniel refers to two different breeds of dogs, both of which are commonly called simply "Springer Spaniel":

Spot Fetcher: Spot "Spotty" Fetcher (March 17, 1989 – February 21, 2004) was one of former U.S. President George W. Bush's dogs.  She was an English Springer Spaniel, named after Scott Fletcher, a former baseball player with the Texas Rangers, a team George W. Bush owned before becoming Governor of Texas in 1994.

Harrier (dog): The Harrier is a medium-sized dog breed of the hound class,

Question: Is it true or false that both the Harrier and English Springer Spaniel are hound dogs?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_statement": {
      "type": "string",
      "description": "The original statement from the question."
    },
    "is_true": {
      "type": "boolean",
      "description": "True if the statement is correct, false otherwise."
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation for why the statement is true or false, based on the provided context."
    },
    "breeds_evaluated": {
      "type": "array",
      "description": "Details about each breed mentioned in the question and its classification.",
      "items": {
        "type": "object",
        "properties": {
          "breed_name": {
            "type": "string",
            "description": "The name of the dog breed."
          },
          "breed_type": {
            "type": "string",
            "description": "The classification or type of the breed as described in the context."
          }
        },
        "required": [
          "breed_name",
          "breed_type"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "question_statement",
    "is_true",
    "reasoning",
    "breeds_evaluated"
  ],
  "additionalProperties": false
}
