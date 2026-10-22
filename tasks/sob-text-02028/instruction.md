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
Norwich park and ride: Norwich Park and Ride is a park & ride bus service in the English city of Norwich, East Anglia.  The first of the park and rides was opened in the early 1990s at Norwich International Airport in Hellesdon, while the sixth (and currently final) site was opened in Thickthorn in 2005.  With the addition of the final site, the Norwich Park & Ride became the largest park and ride services in the United Kingdom, and provided the scheme with over 5,000 permanent car parks – at the time the highest number for a park and ride scheme in the country.  The scheme has proven to be quite successful, winning the British Parking Association Park and Ride award in 2004, and in the 2006/2007 financial year, 3.3 million people used the service, keeping 940,000 cars out of the city centre.

Norwich Pharmacal Co v Customs and Excise Comrs: Norwich Pharmacal Co. & Others v Customs and Excise Commissioners [1974] AC 133 was a case involving the owner and exclusive licensee of a patent, which was infringed by unknown importers of the chemical into the United Kingdom.  Norwich Pharmacal Co brought proceedings against the Excise Commissioners to force the disclosure of information which would identify the importer of the chemical, and therefore those who infringed the patent.  The House of Lords held that where an innocent third party had information relating to unlawful conduct, a court could compel them to assist the person suffering damage by giving them that information.  The case established the Norwich Pharmacal jurisdiction and disclosure orders against innocent third parties are now known as Norwich Pharmacal orders in the UK.

Norfolk Terrier: The Norfolk Terrier is a British breed of dog.  Prior to gaining recognition as an independent breed in 1964, it was a variety of the Norwich Terrier, distinguished from the "prick eared" Norwich by its "drop ears" (or folded ears).  Together, the Norfolk and Norwich Terriers are the smallest of the working terriers.

Norwich School (independent school): Norwich School (formally King Edward VI Grammar School, Norwich) is a selective English independent day school in the close of Norwich Cathedral, Norwich.  Among the oldest schools in the United Kingdom, it has a traceable history to 1096 as an episcopal grammar school established by Herbert de Losinga, first Bishop of Norwich.  In the 16th century the school came under the control of the city of Norwich and moved to Blackfriars' Hall following a successful petition to Henry VIII.  The school was refounded in 1547 in a royal charter granted by Edward VI and moved to its current site beside the cathedral in 1551.  In the 19th century it became independent of the city and its classical curriculum was broadened in response to the declining demand for classical education following the Industrial Revolution.

Airedale Terrier: The Airedale Terrier (often shortened to "Airedale"), also called Bingley Terrier and Waterside Terrier, is a dog breed of the terrier type that originated in the valley ("dale") of the River Aire, in the West Riding of Yorkshire, England.  It is traditionally called the "King of Terriers" because it is the largest of the terrier breeds.  The Airedale was bred from the Old English Black and Tan Terrier (now extinct), the Bull Terrier, the Otterhound and probably some other Terrier breeds, originally to serve as an all around working farm dog.  In Britain this breed has also been used as a war dog, guide dog and police dog.  In the United States, this breed has been used to hunt big game, upland birds, and water fowl, and serve in many other working capacities.

Morkie: The Morkie is a designer breed of dog which is a cross between a purebred Yorkshire terrier and a purebred Maltese.  Another name for this breed is the Morkshire Terrier.  This crossbreed originated in the United States.  In addition, Morkies can be bred with each other.  The Morkie hybrid breed is not recognized by the American Kennel Club as a “bona fide” breed of dog.

Brazilian Terrier: The Brazilian Terrier, is a breed of dog developed in Brazil.  It is one of several terriers probably descended from the combining of the Fox Terrier with other small breeds.

Norwich Terrier: The Norwich Terrier is a breed of dog originating in the United Kingdom, and was bred to hunt small vermin or rodents.  With a friendly personality, Norwich Terriers are today mostly a companion dog breed.  One of the smallest terriers, these dogs are generally healthy, but are relatively rare, due in part to their low litter size and the common need for caesarian sections.  Their drop-eared variety is the Norfolk Terrier.

Parson Russell Terrier: The Parson Russell Terrier is a breed of small white terrier that was the original Fox Terrier of the 18th century.  The breed is named after the person credited with the creation of this type of dog, the Reverend John "Jack" Russell.  It is the recognised conformation show variety of the Jack Russell Terrier and was first recognised in 1990 in the United Kingdom as the Parson Jack Russell Terrier.  In America, it was first recognised as the Jack Russell Terrier in 1997.  The name was changed to its current form in 1999 in the UK and by 2008 all international kennel clubs recognised it under the new name.

Skye Terrier: The Skye Terrier is a breed of dog that is a long, low, hardy terrier and "one of the most endangered native dog breeds in the United Kingdom" according to The Kennel Club.

Question: Which dog originated in the United Kingdom, Norwich Terrier or Brazilian Terrier?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_asked": {
      "type": "string",
      "description": "The original question posed."
    },
    "dog_breeds_compared": {
      "type": "array",
      "description": "Details about the dog breeds mentioned in the question.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the dog breed."
          },
          "origin_country": {
            "type": "string",
            "description": "The country where the dog breed originated."
          },
          "is_uk_origin": {
            "type": "boolean",
            "description": "True if the dog breed originated in the United Kingdom, false otherwise."
          }
        },
        "required": [
          "name",
          "origin_country",
          "is_uk_origin"
        ],
        "additionalProperties": false
      }
    },
    "answer_breed_name": {
      "type": "string",
      "description": "The name of the dog breed that originated in the United Kingdom."
    },
    "answer_reasoning": {
      "type": "string",
      "description": "Explanation for why the answer breed was chosen based on its origin."
    }
  },
  "required": [
    "question_asked",
    "dog_breeds_compared",
    "answer_breed_name",
    "answer_reasoning"
  ],
  "additionalProperties": false
}
