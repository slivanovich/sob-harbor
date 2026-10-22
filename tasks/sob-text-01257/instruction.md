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
Taro: Taro ( ) commonly refers to the plant "Colocasia esculenta", the most widely cultivated species of several plants in the Araceae family which are used as vegetables for their corms, leaves, and petioles.  Thus, this article describes the "dasheen" form of taro; another variety of taro is known as eddoe or "Colocasia antiquorum".  Other species of taro include giant taro ("Alocasia macrorrhizos"), swamp taro ("Cyrtosperma merkusii"), and arrowleaf elephant's ear ("Xanthosoma sagittifolium").

Phyllocladus alpinus: Phyllocladus alpinus, the mountain toatoa or mountain celery pine, is a species of conifer in the Podocarpaceae family.  It is found only in New Zealand.  The form of this plant ranges from a shrub to a small tree of up to seven metres in height.  An example occurrence of "P. alpinus" is within the understory of beech/podocarp forests in the north part of South Island, New Zealand.

Phyllocladus: Phyllocladus, the celery pines, is a small genus of conifers, now usually treated in the family Podocarpaceae."  "Species occur mainly in New Zealand, Tasmania, and Malesia in the Southern Hemisphere, though "P. hypophyllus "ranges into the Philippines, a short way north of the equator.

Phyllocladus toatoa: Phyllocladus toatoa, known as toatoa (Māori) or blue celery pine is a species of conifer in the Podocarpaceae family, endemic to New Zealand.  It was formerly referred to as "P. glaucus".

Bánh pía: Bánh bía, sometimes spelled bánh pía, is a type of Vietnamese cuisine bánh.  A Suzhou style mooncake adapted from Teochew cuisine.  The Vietnamese name comes from the Teochew word for pastry, "pia".  In Saigon, the pastry is called “bánh bía” while in Sóc Trăng and Vũng Thơm it is known by "bánh Pía".  Some Vietnamese call it bánh lột da, which translates to "peeling flakes pastry", and those from the Bến Tre region call it bánh bao chi, which is the name for Mochi elsewhere in Vietnam.  Popular fillings include durian, shredded pork fat, salted egg yolk, mung bean paste, taro and coconut.

Imoni: Imoni (芋煮 ) is a type of taro and meat soup eaten traditionally in the autumn in the Tōhoku region of Japan.  Yamagata Prefecture in particular is famous for its imoni, but other prefectures in the region also have their own different varieties.

Phyllocladus hypophyllus: Phyllocladus hypophyllus is a species of conifer in the Podocarpaceae family.

Sago soup: Sago soup or Sai mai lou is a type of tong sui dessert in Cantonese cuisine, which is also a variant of tapioca pudding.  It is basically made by pearl tapioca (sago), coconut milk and evaporated milk.  The dish is traditionally prepared using sago starch, which is derived from sago palm pith.  Other ingredients can also be added, such as taro, pumpkin, mango, etc.

Phylloclade: Phylloclades and cladodes are flattened, photosynthetic shoots, which are usually considered to be modified branches.  The two terms are used either differently or interchangeably by different authors. " Phyllocladus", a genus of conifer, is named after these structures.  Phylloclades/cladodes have been identified in fossils dating from as early as the Permian.

Kalua: Kālua is a traditional Hawaiian cooking method that utilizes an imu, a type of underground oven.  The word "kālua", which literally means "to cook in an underground oven", may also be used to describe the food cooked in this manner, such as kālua pig or kālua turkey, which are commonly served at luau feasts.  Luau, in Hawaiian is actually the name of the taro leaf, which when young and small after being steamed for a couple hours resembles cooked spinach.  The traditional luau was eaten on the floor over lauhala (leaves of the hala tree were weaved together) mats.

Question: Which is a type of conifer, Taro or Phyllocladus?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "identified_conifer_name": {
      "type": "string",
      "description": "The name of the plant identified as a conifer."
    },
    "is_taro_a_conifer": {
      "type": "boolean",
      "description": "Indicates whether Taro is a conifer based on the context."
    },
    "conifer_details": {
      "type": "object",
      "properties": {
        "genus": {
          "type": "string",
          "description": "The genus name of the conifer."
        },
        "family": {
          "type": "string",
          "description": "The family the conifer belongs to."
        },
        "description_excerpt": {
          "type": "string",
          "description": "A brief description of the conifer from the context."
        }
      },
      "required": [
        "genus",
        "family",
        "description_excerpt"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "identified_conifer_name",
    "is_taro_a_conifer",
    "conifer_details"
  ],
  "additionalProperties": false
}
