# PII Reference — Severity Classification

Personal Identifiable Information (PII) is any information that can identify an
individual, either directly or when combined with other data. The severity categories
below guide how to classify findings. The examples listed under each category are
**illustrative, not exhaustive** — apply judgment to any information that could
identify a real person, even if it doesn't match these examples exactly.

## Severity Levels

### Critical

Information that, when exposed, can directly and uniquely re-identify a specific
individual, typically enabling identity theft or serious harm with little additional
data needed.

Types that commonly fall at this level include (but are not limited to):
- Government-issued identity numbers (national ID, social security number, tax
  identification number)
- Passport and national identity document numbers
- Driver's license and similar government-issued permit numbers
- Biometric data (fingerprint templates, facial recognition vectors, retinal scans)
- Full name combined with two or more other identifiers (e.g., name + date of birth
  + address, or name + SSN)
- Medical record numbers or health insurance identifier numbers
- Financial instrument numbers tied to an individual (full credit card number with
  CVV, bank account numbers)

### High

Information that directly identifies or enables contact with a specific individual,
creating significant privacy risk if exposed.

Types that commonly fall at this level include (but are not limited to):
- Email addresses (especially personal or combined with other personal data)
- Full home or workplace addresses
- Phone numbers (mobile, direct landline)
- Full date of birth
- Login credential pairs (username together with a password or PIN)
- Financial account numbers (IBAN, account number alone)
- IP addresses that resolve to an identifiable individual or household

### Medium

Information that alone may not pinpoint an individual but is clearly personal and
increases identification risk when combined with other data.

Types that commonly fall at this level include (but are not limited to):
- Full name (alone, without contact details or other identifiers)
- Date of birth without accompanying name or address
- Precise GPS coordinates or neighborhood-level location data
- Ethnic or racial origin
- Religious or political beliefs or affiliations
- Health conditions, diagnoses, or medical history
- Employment or educational history details
- Sexual orientation or gender identity

### Low

Information that is only marginally identifying by itself but may contribute to
re-identification in aggregate or when combined with other data.

Types that commonly fall at this level include (but are not limited to):
- Job title or department (without employer name or contact details)
- Age range (e.g., "30–35 years old")
- General geographic region (city or country level)
- Nationality or citizenship
- Publicly known preferences, affiliations, or memberships without direct contact
  information

## Applying These Categories

These categories are starting points for judgment, not rigid rules. Context matters:

- **Aggregate risk**: Multiple Low or Medium items appearing in the same document
  can collectively constitute High or Critical exposure — evaluate the combination,
  not just individual items.
- **Pseudonymized data**: User IDs or hashed values without an accompanying lookup
  table are typically Low risk or no risk; re-evaluate if a mapping table is also
  present or accessible.
- **Role of context**: A name in a public press release is not PII in any meaningful
  sense; the same name in a private medical record is High or Critical.
- **Combination effects**: Date of birth alone is Medium; paired with postal code
  and gender it can uniquely identify most individuals — treat the combination as
  Critical.
