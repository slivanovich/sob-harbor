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
Shōnen to Inu: Shōnen to Inu (少年と犬 ) is a Japanese manga written by Akira Itō and illustrated by Yoshihiro Takahashi.  The manga was re-issued in 2001 under the name Ginga no Inutachi [Shōnen to Inu] Remix (銀牙の犬たち [少年と犬] リミックス ) .  It has six different stories about six different dog breeds: Golden Retriever, Shiba Inu, Siberian Husky, German Shepherd, Labrador Retriever and Great Pyrenees.  All stories are mostly about the relationships between the dogs and a boy or a young man.

Thai cat: The Thai cat or Wichien Maat (Thai: วิเชียรมาศ ,  ] , rtgs: wichianmat , meaning 'moon diamond') is a newly renamed but old cat breed, related to but distinct from the Western, modern Siamese cat.  This natural breed is descended from the landrace of "wichianmat " cats of Thailand, and as a standardised breed has also been variously called the Old-style, Old-type, Traditional, or Classic Siamese; the Whichian Mat (anglicised from the Thai name); and the Applehead, a nickname that originated as a pejorative used by breeders of the modern-style Siamese.  According to The International Cat Association: "The Thai is the breed dedicated to preserving the native pointed cat of Thailand in as close to its original form as possible."

Phyllis McCarthy: Phyllis McCarthy (12 March 1903 Johannesburg – 16 February 1986 Johannesburg) was a noted South African breeder of and authority on Rhodesian Ridgeback dogs.  She established the Glenaholm Kennels in 1949 in Pietermaritzburg, South Africa, played a seminal role in the Ridgeback community and produced a long line of Ridgebacks featuring prominently in the ancestry of almost all modern members of the breed.

Thai Ridgeback: The Thai Ridgeback (Thai: ไทยหลังอาน , rtgs: Thai Lang-An ) is an ancient landrace of dog, recently established also as a standardized breed.  The breed was formerly unknown outside of Thailand, but is gaining notice in the Western world.  They are also known as a Mah Thai Lang Ahn.  The Thai Ridgeback is one of only three breeds that has a ridge of hair that runs along its back in the opposite direction to the rest of the coat.  The other two are the Rhodesian Ridgeback and the Phu Quoc Ridgeback.

Kathoey: Kathoey or katoey (Thai: กะเทย ; rtgs: "Kathoei"  ] ) is a transgender woman or an effeminate gay male in Thailand.  A significant number of Thais perceive "kathoeys" as belonging to a third gender, including many "kathoeys" themselves, while others see them as either a kind of man or a kind of woman.  However, when considering transgender women (MtF) as a group in Thai society, most refer to themselves as "phuying" (Thai: ผู้หญิง "women"), with a minority referring to themselves as "phuying praphet song" (a "second kind of woman") and only very few referring to themselves as "kathoey".  Related phrases include "phet thi sam" (Thai: เพศที่สาม , "third gender"), and "sao praphet song" or "phu ying praphet song" (Thai: สาวประเภทสอง, ผู้หญิงประเภทสอง — both meaning "second-type female").  The word "kathoey" is of Khmer origin.  It is most often rendered as ladyboy or lady boy in English conversation with Thais and this latter expression has become popular across Southeast Asia.

Phu Quoc Ridgeback: The Phu Quoc Ridgeback is a breed of dog from Phú Quốc Island in Vietnam's southern Kiên Giang Province.  The Phu Quoc Ridgeback is one of only three breeds that has a ridge of hair that runs along its back in the opposite direction from the rest of the coat (the others are Rhodesian Ridgeback and Thai Ridgeback).  The Phu Quoc is the smallest of the three ridgeback breeds.

Great Pyrenees: The Pyrenean Mountain Dog, known as the Great Pyrenees in North America, is a large breed of dog used as a livestock guardian dog.  It should not be confused with the Pyrenean Mastiff.

Nom yen: Nom Yen (Thai: นมเย็น) is a Thai drink made from Sala syrup and hot milk.  Nom in Thai means milk.  There are two kind of milk for making Nom Yen.  "Nom sot is fresh milk, nom tamada is condensed milk, and nom kom is sweetened condensed milk" There are two styles of Nom Yen which are iced and frappe ones.  You can find it at almost everywhere in Thailand from vendors selling drinks on street.  "The price ranges from 15 THB (Thai baht) to 25 THB alone or from 30 to 60 THB at a café with some bakery" Thai people also make sweet from nom Yen as well.  The other style of Nom Yen can be found in street sweet shops.  It's called "Nam Kang Sai" or a Thai style frozen Nom Yen.  The ingredients are similar to Nom Yen, except changing from iced into frozen one.  Unlike Nom Yen, Thai people consider Nam Kang Sai a homemade style sweet because it's easy to make and the ingredients can be found easily in local area.

King Shepherd: The King Shepherd is a dog breed developed from crossing German Shepherd Dog with Shiloh Shepherd and long-coated European lines of German Shepherd along with the Great Pyrenees in the 1990s.

Pyrenean Shepherd: The Pyrenean Shepherd (known in France originally, and also in non-AKC registries such as the UKC, as the Berger des Pyrénées, and in Spain as the Pastor de los Pirineos) is a medium-small breed of dog native to the Pyrenees mountains in southern France and northern Spain, bred since at least medieval times for herding livestock, especially sheep.  It worked as an active herder together with the Great Pyrenees, another mountain dog, which acted as the flock's guardian.

Question: Great Pyrenees and Thai Ridgeback, are both which kind of breed of animal?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "common_animal_type": {
      "type": "string",
      "description": "The common animal type for all breeds mentioned in the question."
    },
    "queried_breeds": {
      "type": "array",
      "description": "A list of the specific breeds mentioned in the question.",
      "items": {
        "type": "string"
      }
    },
    "breed_information": {
      "type": "array",
      "description": "Detailed information about each breed mentioned.",
      "items": {
        "type": "object",
        "properties": {
          "breed_name": {
            "type": "string",
            "description": "The name of the breed."
          },
          "animal_category": {
            "type": "string",
            "description": "The specific animal category this breed belongs to."
          },
          "is_ridgeback_breed": {
            "type": "boolean",
            "description": "Indicates if the breed is one of the three known ridgeback breeds."
          },
          "origin_country_or_region": {
            "type": "string",
            "description": "The country or region of origin for the breed."
          }
        },
        "required": [
          "breed_name",
          "animal_category",
          "is_ridgeback_breed",
          "origin_country_or_region"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "common_animal_type",
    "queried_breeds",
    "breed_information"
  ],
  "additionalProperties": false
}
