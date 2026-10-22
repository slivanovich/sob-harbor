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
Pardis Animal Shelter: Pardis Animal Shelter (Persian: پناهگاه حیوانات پردیس‎ ‎ ) is a no-kill animal shelter, a spay/neuter clinic, and a public animal hospital located near Tabriz, Iran.  It is affiliated with "Tabriz Society for the Prevention of Cruelty to Animals" which is a volunteer nonprofit organization based in Tabriz, devoted to pet adoption and animal rescue.  Pardis Shelter was founded by Jila Pourirani in 2012, after a massive cull that nearly 400 dogs were shot dead in Tabriz.  Pardis Shelter has a clinic, 11 shelters, three niches and shaded areas.  1300 animals of different kinds including dogs, cats, foxes, horses and birds such as eagle, owl and vultures are being treated and sheltered in this center.

Pet adoption: Pet adoption is the process of taking responsibility for a pet that a previous owner has abandoned or released to a shelter or rescue organization.  Common sources for adoptable pets are animal shelters and rescue groups.  Some organizations give adopters ownership of the pet, while others use a guardianship model wherein the organization retains some control over the animal's future use or care.

Students for Saving Social Security: Students for Saving Social Security, known as S4, was a 501(c)(3) non-profit activist organization based in Washington, D.C., run by students for students pushing for Social Security reform.  S4 was founded in March 2005 and proposed changing Social Security laws to permit personal savings accounts.  The organization had a network of 300+ college chapters with more than 11,000 members by 2008.

American Atheists: American Atheists is a non-profit activist organization in the United States dedicated to defending the civil liberties of atheists and advocating for the complete separation of church and state.  It provides speakers for colleges, universities, clubs and the news media.  It also publishes books and the quarterly "American Atheist Magazine", currently edited by Pamela Whissel.  The organization was founded by Madalyn Murray O'Hair in 1963, following her role in removing mandatory prayer from public schools.

Adopt-a-Pet.com: Adopt-a-Pet. com is a North America’s largest non-profit pet-adoption web service that advocates pet adoption, gathering information from over 12,000 pet shelters in the U.S. and Canada, and presenting adoptable pet data in a searchable data base to facilitate pet adoption.  Adopt-a-pet. com is registered in Redondo Beach, California, as Humane America Animal Foundation.  The web site allows people to sign up to receive an email when a pet that satisfies their criteria appears in a local shelter.  Adopt-a-Pet. com also contains information on pet care for first-time pet owners and publishes a newsletter.  The web site also lists volunteer opportunities and promotes spaying and neutering of the pets.

Croatian Amateur Radio Association: The Croatian Amateur Radio Association (Croatian: "Hrvatski radioamaterski savez" , HRS) is a national non-profit organization for amateur radio enthusiasts in Croatia.  Key membership benefits of HRS include the sponsorship of amateur radio operating awards and radio contests.  HRS also supports local competitions in Amateur Radio Direction Finding as well as a national team that travels to regional and world championship events.  HRS will be the sponsoring organization for the 2010 Amateur Radio Direction Finding World Championships to be held in Dubrovnik.  HRS represents the interests of Croatian amateur radio operators before Croatian and international telecommunications regulatory authorities.  HRS is the national member society representing Croatia in the International Amateur Radio Union.

Best Friends Animal Society: Best Friends Animal Society, founded in its present form in 1991, is an American nonprofit 501(c)(3) animal welfare organization.  Best Friends works nationwide in outreach programs with shelters, rescue groups and members to promote pet adoption, no-kill animal rescue, and spay-and-neuter practices.

House Rabbit Society: The House Rabbit Society (HRS) is a non-profit activist organization based in Richmond, California, United States (US), that rescues and adopts rabbits and educates the community with its curriculum on rabbit care.  HRS promotes responsible rabbit ownership, including the spaying and neutering of all pet rabbits, proper veterinary care, diet, and exercise.  HRS takes the stand that domestic rabbits should not live outdoors. ] .

Berkshire Humane Society: The Berkshire Humane Society (BHS) is a private non-profit humane organization in Berkshire County, Massachusetts.  Founded in 1992, BHS is an open admissions shelter and has cared for over 43,000 animals.  The humane society operates animal welfare services and pet adoption facilities in Pittsfield and Great Barrington.

Loving Companions Animal Rescue, Inc.: Loving Companions Animal Rescue, Inc. (LCAR) is a non-profit, no-kill animal rescue shelter located in North Pole, Alaska.  They provide a safe place to care for animals who are unwanted and abandoned.  LCAR animals are cared for by volunteers who offer their time by providing facility maintenance needs, assist with social media sites, and/or open their homes as animal foster parents.  The goal of Loving Companions is to promote a better life for animals, and provide the community an alternative to euthanizing unwanted animals.  LCAR’s promotion of a better life for animals include pet adoption, animal foster care, and providing low-income pet owners with services such as assistance with pet food, free boarding, and more.

Question: The House Rabbit Society (HRS) is a non-profit activist organization, it rescues and does pet adoption, the process of taking responsibility for a pet, based in Richmond, in what state?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "organization_name": {
      "type": "string",
      "description": "The name of the organization."
    },
    "organization_type": {
      "type": "string",
      "description": "The type of the organization."
    },
    "location_city": {
      "type": "string",
      "description": "The city where the organization is based."
    },
    "location_state": {
      "type": "string",
      "description": "The state where the organization is based."
    },
    "primary_activities": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of the primary activities of the organization."
    }
  },
  "required": [
    "organization_name",
    "organization_type",
    "location_city",
    "location_state",
    "primary_activities"
  ],
  "additionalProperties": false
}
