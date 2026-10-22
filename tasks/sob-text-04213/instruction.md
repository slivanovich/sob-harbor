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
Barnyard Dawg: (The) Barnyard Dawg (also known as George P. Dog) is a "Looney Tunes" character.  An adult anthropomorphic basset hound, he is the archenemy of Foghorn Leghorn.  He was created by Robert McKimson, who also created Foghorn, and was voiced by Mel Blanc.  Dawg also feuds with other enemies as well like Henery Hawk, the Weasel, Daffy Duck and Sylvester.  He appeared in 22 Golden Age–era Warner Bros. shorts.

Stephens Cur: The Stephens Cur (a.k.a. Stephens' Stock Cur), is a scent hound that belongs to the Cur dog breed.  They were originally bred by the Stephens family in southeastern Kentucky.  The dogs known as "Little black dog" were bred by generations of that family for over a century.  In 1970, they were recognized as separate and distinct breed of Cur.  The dog is mostly black with white markings, but more than a third white is not permissible.  It is good for hunting raccoon and squirrel, but can also be used to bay wild boar.  They are registered with the United Kennel Club

Basset Hound: The Basset Hound is a short-legged breed of dog of the hound family.  The Basset is a scent hound that was originally bred for the purpose of hunting hare.  Their sense of smell and ability to ground-scent is second only to that of the Bloodhound.  Basset Hounds are one of 6 recognised basset-type breeds in France.

Uncle Earl's Hog Dog Trials: Uncle Earl's Hog Dog Trials is an annual Hog Dog Baying Event held in the third weekend of March in Winnfield, Winn Parish, Louisiana at the Winn Parish Fair Grounds involving boars and various breeds of bay dogs, including Catahoula Leopard Dogs, Blackmouth Cur, Blue Lacy, and others.

Dog Tales (1958 film): Dog Tales is a 1958 Warner Brothers animated cartoon which consists of a series of blackout gags involving dogs (e.g., one in which a doberman pinscher viciously pinches an overweight U.S. Army private identified as "Doberman" (a reference to, and caricature of, the character played by Maurice Gosfield on "The Phil Silvers Show"); and another in which the narrator can't make up his mind whether the dog pictured is a pointer or a setter, and then finally shows a picture of a "point-setter").  A basset hound declares that she's a TV star (a reference to Cleo the Dog, from the contemporary TV sitcom "The People's Choice"), we learn the unusual breed of a Newfoundland puppy's grandfather, and a great dane named "Victor Barky" plays the piano.  Reused animation from Chuck Jones' "Often an Orphan" (1949) and Friz Freleng's "Piker's Peak" (1957) is also seen here.  In the former case, Charlie Dog makes a cameo - his final appearance in a Warner Bros. cartoon as well as his only cartoon to not be directed by Chuck Jones.  This animated film features the voices of Mel Blanc, Robert C. Bruce and Julie Bennett, and was directed by Robert McKimson and written by Tedd Pierce.  It was released in theaters on July 26, 1958.

Fred Basset: Fred Basset is a comic strip about a male basset hound.  The cartoon was created by Scottish cartoonist Alex Graham and published first in the "Daily Mail" on 8 July 1963.  It has since been syndicated around the world.

Catahoula bulldog: The Catahoula bulldog is a crossbreed dog created by crossing the Catahoula Cur and the American Bulldog.

Freedom Planet: Freedom Planet is a two-dimensional platform video game developed and published by independent developer GalaxyTrail.  The player controls one of three anthropomorphic animal protagonists: the dragon Lilac, the wildcat Carol, or the basset hound Milla.  Aided by the duck-like Torque, the player attempts to defeat Lord Brevon, who plans to conquer the galaxy.  While the game focuses on fast-paced platforming, its levels are interspersed with slower action scenes.

Catahoula Cur: The Catahoula Cur is an American dog breed named after Catahoula Parish, Louisiana, United States.  Also known as the Catahoula Leopard Dog, it became the state dog of Louisiana in 1979.  The breed is sometimes referred to as the "Catahoula Hound" or "Catahoula Leopard Hound" because of its spots, although it is not a true hound but a cur.  It is also called the "Catahoula Hog Dog", reflecting its traditional use in hunting wild boar.

Mountain Cur: The Mountain Cur is a type of working dog that is bred specifically for treeing and trailing small game, like squirrel and raccoons.  They are also used for hunting and baying big game like bear and wild boar as well as being an all-purpose farm dog.  Curs are a member of the Hound group, and the Mountain Cur is one of several varieties of cur.  It can also be used as a water dog.  Mainly bred in Ohio, Kentucky, Virginia, and Tennessee, it has been registered with the United Kennel Club since 1998.  The Mountain Cur Breeder's Association was formed in 1957.

Question: Are both Catahoula Cur and Basset Hound types of dogs?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "are_both_dog_types": {
      "type": "boolean",
      "description": "Indicates whether both Catahoula Cur and Basset Hound are confirmed as types of dogs."
    },
    "dog_type_confirmations": {
      "type": "array",
      "description": "Details confirming each specified breed as a type of dog.",
      "items": {
        "type": "object",
        "properties": {
          "breed_name": {
            "type": "string",
            "description": "The name of the dog breed."
          },
          "is_a_dog_type": {
            "type": "boolean",
            "description": "True if the breed is confirmed as a type of dog."
          },
          "confirmation_source": {
            "type": "string",
            "description": "A direct quote or phrase from the context confirming it is a dog type."
          }
        },
        "required": [
          "breed_name",
          "is_a_dog_type",
          "confirmation_source"
        ],
        "additionalProperties": false
      }
    },
    "number_of_breeds_evaluated": {
      "type": "integer",
      "description": "The total number of dog breeds evaluated in the question."
    }
  },
  "required": [
    "are_both_dog_types",
    "dog_type_confirmations",
    "number_of_breeds_evaluated"
  ],
  "additionalProperties": false
}
