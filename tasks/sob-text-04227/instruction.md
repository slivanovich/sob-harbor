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
Australian Terrier: The Australian Terrier is a small breed of dog of the terrier dog type.  The breed was developed in Australia, although the ancestral types of dogs from which the breed descends were from Great Britain.

Australian Silky Terrier: The Australian Silky Terrier is a small breed of dog of the terrier dog type.  The breed was developed in Australia, although the ancestral types and breeds were from Great Britain.  It is closely related to the Australian Terrier and the Yorkshire Terrier.  The breed is called the "Silky Terrier" in North America, but is called the "Australian Silky Terrier" in its country of origin and in the rest of the world.

Terrier Group: Terrier Group is the name of a breed Group of dogs, used by kennel clubs to classify a defined collection of dog breeds.  In general, a "Terrier Group" includes one particular type of dog, the Terrier, although other types may be included in a kennel club's "Terrier Group".  Most major English-language kennel clubs include a "Terrier Group" although different kennel clubs may not include the same breeds in their "Terrier Group".  The international kennel club association, the Fédération Cynologique Internationale, includes Terriers in Group 3 "Terrier", which is then further broken down into four "Sections" based on the type of terrier and breed history.

Teddy Roosevelt Terrier: The Teddy Roosevelt Terrier is a small to medium-sized American hunting terrier.  Lower-set with shorter legs, more muscular, and heavier bone density than its cousin the American Rat Terrier.  There is much diversity in the history of the Teddy Roosevelt Terrier breed and it shares a common early history with the American Rat Terrier, Fox Paulistinha and Tenterfield Terrier.  It is said the Rat Terrier background stems from the terriers or other dogs that were brought over by early English and other working class immigrants.  Since the breed was a farm, hunting and utility dog there was little to no planned breeding other than breeding dogs with agreeable traits to each other in order to produce the desired work ethic in the dog.  It is assumed that the Feist (dog), Bull Terrier, Smooth Fox Terrier, Manchester Terrier, Whippet, Italian Greyhound, the now extinct English White Terrier, Turnspit dog and or Wry Legged Terrier all share in the Teddy Roosevelt Terrier's ancestry.  These early Ratting Terriers were then most likely bred to the Beagle or Beagle cross bred dogs (for increased scenting ability) and other dogs.  Maximizing the influences from these various breeds provides the modern Teddy Roosevelt Terrier with a keen sense of awareness and prey drive, an acute sense of smell and a very high intellect.  Although they tend to be aloof with strangers they are devoted companion dogs with a strong desire to please and be near their owners side at all times.

Himalayan Sheepdog: The Himalayan Sheepdog, also referred to as the Bhote Kukur or Bhotia, is a livestock guardian dog that originated from Nepal.  This mountain dog breed is closely similar to Indian Mastiff and the Tibetan Mastiff and may be related to the long-haired Kinnaur Sheepdog of Tibet.  Naturally, Himalayan Sheepdogs enjoy outdoor lifestyles and are rarely seen beyond the regions of India and Nepal.  As a powerful and robust breed, the Himalayan Sheepdog is mainly used for herding purposes.  The Himalayan Sheepdog is regionally popular as both a loyal companion as well as a working dog.

Airedale Terrier: The Airedale Terrier (often shortened to "Airedale"), also called Bingley Terrier and Waterside Terrier, is a dog breed of the terrier type that originated in the valley ("dale") of the River Aire, in the West Riding of Yorkshire, England.  It is traditionally called the "King of Terriers" because it is the largest of the terrier breeds.  The Airedale was bred from the Old English Black and Tan Terrier (now extinct), the Bull Terrier, the Otterhound and probably some other Terrier breeds, originally to serve as an all around working farm dog.  In Britain this breed has also been used as a war dog, guide dog and police dog.  In the United States, this breed has been used to hunt big game, upland birds, and water fowl, and serve in many other working capacities.

Kerry Blue Terrier: The Kerry Blue Terrier (also known as the Irish Blue Terrier) () is a breed of dog.  Originally bred to control "vermin" including rats, rabbits, badgers, foxes, otters and hares, over time the Kerry became a general working dog used for a variety of jobs including herding cattle and sheep, and as a guard dog.  Today the Kerry has spread around the world as a companion and working dog.  Despite a Kerry Blue winning Crufts (the most important UK dog show) in 2000, it remains an "unfashionable" breed, and is distinctly uncommon; however, it not as threatened as some of the other terrier breeds such as Skye Terrier, Sealyham Terrier, and Dandie Dinmont Terrier.

Vulnerable Native Breeds: Vulnerable Native Breeds are a group of dog breeds originating in the United Kingdom and Ireland, and identified by The Kennel Club (KC) as having annual registration numbers of 300 puppies or fewer.  The need for such a list was first identified in June 2003, with research conducted by the KC to identify the extent of the vulnerability and viability of each breed.  It was a joint project, with the KC working with the British and Irish Native Breeds Trust, later to be known simply as the Native Dog Breeds Trust.  The breeds on the list have been promoted at events such as Discover Dogs and Crufts, and by asking that owners of these breeds mate their dogs rather than having them spayed.

Fox Terrier: Fox Terriers are two different breeds of the terrier dog type: the Smooth Fox Terrier and the Wire Fox Terrier.  Both of these breeds originated in the 19th century from a handful of dogs who are descended from earlier varieties of British terriers, and are related to other modern white terrier breeds.  In addition, a number of breeds have diverged from these two main types of fox terrier and have been recognised separately, including the Jack Russell Terrier, Miniature Fox Terrier and Rat Terrier.  The Wire and Smooth Fox Terriers share similar characteristics, the main differences being in the coat and markings.  They have been successful in conformation shows, more prominently in America than their homeland.

Tugou: Tugou (土狗, pinyin: "tǔ gǒu"), literally means Native Dog in Mandarin Chinese, is the general name for several dog breeds originated from China and still abundantly exists across the country today.  Tugou includes the most popular Chinese dog breed - the Chinese Field Dog (, pinyin: "zhōng huá tián yuán quǎn"), Chinese Chongqing Dog, Xiasi Dog, and several other native dog breeds distributed across China.  They are roughly 45–50 cm tall at the shoulder.

Question: Are both Himalayan Sheepdog and Australian Terrier examples of dog breeds?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "is_both_dog_breeds": {
      "type": "boolean",
      "description": "True if both mentioned entities are confirmed as dog breeds, false otherwise."
    },
    "breeds_information": {
      "type": "array",
      "description": "Details for each breed mentioned in the question.",
      "items": {
        "type": "object",
        "properties": {
          "breed_name": {
            "type": "string",
            "description": "The name of the dog breed."
          },
          "is_confirmed_dog_breed": {
            "type": "boolean",
            "description": "True if the entity is explicitly identified as a dog breed in the context."
          },
          "origin_country": {
            "type": "string",
            "description": "The country where the breed was developed or originated."
          },
          "dog_type": {
            "type": "string",
            "description": "The general type or classification of the dog breed."
          }
        },
        "required": [
          "breed_name",
          "is_confirmed_dog_breed",
          "origin_country",
          "dog_type"
        ],
        "additionalProperties": false
      }
    },
    "overall_confirmation_statement": {
      "type": "string",
      "description": "A summary statement confirming the status of both breeds."
    }
  },
  "required": [
    "is_both_dog_breeds",
    "breeds_information",
    "overall_confirmation_statement"
  ],
  "additionalProperties": false
}
