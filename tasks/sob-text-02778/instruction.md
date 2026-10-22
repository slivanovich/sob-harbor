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
Airedale Terrier: The Airedale Terrier (often shortened to "Airedale"), also called Bingley Terrier and Waterside Terrier, is a dog breed of the terrier type that originated in the valley ("dale") of the River Aire, in the West Riding of Yorkshire, England.  It is traditionally called the "King of Terriers" because it is the largest of the terrier breeds.  The Airedale was bred from the Old English Black and Tan Terrier (now extinct), the Bull Terrier, the Otterhound and probably some other Terrier breeds, originally to serve as an all around working farm dog.  In Britain this breed has also been used as a war dog, guide dog and police dog.  In the United States, this breed has been used to hunt big game, upland birds, and water fowl, and serve in many other working capacities.

Black Russian Terrier: The Black Russian Terrier (abbreviated as BRT), also known as the Tchiorny Terrier ("tchiorny" being Russian for black) is a breed of dog created in USSR in Red Star (Krasnaya Zvezda) Kennel during the late 1940s and the early 1950s for use as military/working dogs.  At the present time, the Black Russian Terrier is a breed recognized by the FCI (FCI's from September 1983), AKC (AKC's from July 2004), CKC, KC, ANKC, NZKC and other cynological organizations.  The contemporary Black Russian Terrier is a working dog, guarding dog, sporting and companion dog.

Fox Terrier: Fox Terriers are two different breeds of the terrier dog type: the Smooth Fox Terrier and the Wire Fox Terrier.  Both of these breeds originated in the 19th century from a handful of dogs who are descended from earlier varieties of British terriers, and are related to other modern white terrier breeds.  In addition, a number of breeds have diverged from these two main types of fox terrier and have been recognised separately, including the Jack Russell Terrier, Miniature Fox Terrier and Rat Terrier.  The Wire and Smooth Fox Terriers share similar characteristics, the main differences being in the coat and markings.  They have been successful in conformation shows, more prominently in America than their homeland.

Stephens Cur: The Stephens Cur (a.k.a. Stephens' Stock Cur), is a scent hound that belongs to the Cur dog breed.  They were originally bred by the Stephens family in southeastern Kentucky.  The dogs known as "Little black dog" were bred by generations of that family for over a century.  In 1970, they were recognized as separate and distinct breed of Cur.  The dog is mostly black with white markings, but more than a third white is not permissible.  It is good for hunting raccoon and squirrel, but can also be used to bay wild boar.  They are registered with the United Kennel Club

Teddy Roosevelt Terrier: The Teddy Roosevelt Terrier is a small to medium-sized American hunting terrier.  Lower-set with shorter legs, more muscular, and heavier bone density than its cousin the American Rat Terrier.  There is much diversity in the history of the Teddy Roosevelt Terrier breed and it shares a common early history with the American Rat Terrier, Fox Paulistinha and Tenterfield Terrier.  It is said the Rat Terrier background stems from the terriers or other dogs that were brought over by early English and other working class immigrants.  Since the breed was a farm, hunting and utility dog there was little to no planned breeding other than breeding dogs with agreeable traits to each other in order to produce the desired work ethic in the dog.  It is assumed that the Feist (dog), Bull Terrier, Smooth Fox Terrier, Manchester Terrier, Whippet, Italian Greyhound, the now extinct English White Terrier, Turnspit dog and or Wry Legged Terrier all share in the Teddy Roosevelt Terrier's ancestry.  These early Ratting Terriers were then most likely bred to the Beagle or Beagle cross bred dogs (for increased scenting ability) and other dogs.  Maximizing the influences from these various breeds provides the modern Teddy Roosevelt Terrier with a keen sense of awareness and prey drive, an acute sense of smell and a very high intellect.  Although they tend to be aloof with strangers they are devoted companion dogs with a strong desire to please and be near their owners side at all times.

Terrier Group: Terrier Group is the name of a breed Group of dogs, used by kennel clubs to classify a defined collection of dog breeds.  In general, a "Terrier Group" includes one particular type of dog, the Terrier, although other types may be included in a kennel club's "Terrier Group".  Most major English-language kennel clubs include a "Terrier Group" although different kennel clubs may not include the same breeds in their "Terrier Group".  The international kennel club association, the Fédération Cynologique Internationale, includes Terriers in Group 3 "Terrier", which is then further broken down into four "Sections" based on the type of terrier and breed history.

Paisley Terrier: The Paisley Terrier was a breed of terrier type dog that is now extinct.  Originating in Scotland, the Paisley Terrier was bred primarily as a pet and showdog version of the Skye Terrier, and was the progenitor of today's Yorkshire Terrier.  The breed was called the Paisley terrier since most of the dogs came from that location, but it was also called the Clydesdale Terrier, for another location in the Clyde Valley where the dogs were bred.

Pit bull: Pit bull is the common name for a type of dog.  Formal breeds often considered in North America to be of the pit bull type include the American Pit Bull Terrier, American Staffordshire Terrier, American Bully, and Staffordshire Bull Terrier.  The American Bulldog is also sometimes included.  Many of these breeds were originally developed as fighting dogs from cross breeding bull-baiting dogs (used to hold the faces and heads of larger animals such as bulls) and terriers.  After the use of dogs in blood sports was banned, such dogs were used as catch dogs in the United States for semi-wild cattle and hogs, to hunt and drive livestock, and as family companions.  Despite dog fighting now being illegal in the United States, it still exists as an underground activity, and pit bulls are a common breed of choice.

Cesky Terrier: The Cesky Terrier ( ; Czech: "Český teriér", literally "Bohemian Terrier" or "Czech Terrier") is a small terrier type dog originating in Czechoslovakia.

Black Mouth Cur: The Black Mouth Cur is a hunting and cattle dog that has its origins in Southern United States.

Question: Are Cesky Terrier and Black Mouth Cur both dogs?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "are_both_dogs": {
      "type": "boolean",
      "description": "Indicates whether both specified breeds are dogs."
    },
    "dog_breeds_checked": {
      "type": "array",
      "description": "Details for each breed mentioned in the question.",
      "items": {
        "type": "object",
        "properties": {
          "breed_name": {
            "type": "string",
            "description": "The name of the dog breed."
          },
          "is_a_dog": {
            "type": "boolean",
            "description": "True if the context identifies this as a dog breed, false otherwise."
          }
        },
        "required": [
          "breed_name",
          "is_a_dog"
        ],
        "additionalProperties": false
      }
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation for the answer based on the provided context."
    }
  },
  "required": [
    "are_both_dogs",
    "dog_breeds_checked",
    "reasoning"
  ],
  "additionalProperties": false
}
