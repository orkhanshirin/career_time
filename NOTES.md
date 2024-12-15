## Decisions & Assumptions

- **Functional Approach:**  
  - Decided on a functional style rather than OOP to keep the code minimal and testable.
  
- **Single Profile Parsing:**  
  - Initially focused on parsing a single `sample_profile.json` rather than multiple profiles. 
  - Assumption: The main use case is to demonstrate the logic, with multi-profile support to be added later.
  
- **Duration Parsing Logic:**
  - Assumed that all `duration` fields follow a "X years Y months" pattern. If the format changes, the code will need to be updated. 

- **No External Dependencies for Parsing:**
  - Chose not to use third-party libraries for parsing durations to keep dependencies minimal. 
  - Assumption: The input format is stable and does not require complex parsing capabilities.

## Open Points

- **Data Validation:**
  - Currently not validating schema beyond basic checks. Need to clarify if `member_shorthand_name` and `member_experience_collection` are always present.
  
- **Overlapping Experiences:**
  - The code does not handle the possibility of overlapping work periods. It's unclear if we need to consider this in the future. (the top priority optimization)

- **Date Ranges vs Durations:**
  - Currently relying on provided `duration` fields. If they become unavailable or inconsistent, we need to discuss on whether to calculating durations from `date_from` and `date_to` fields.

## Limitations

- **Single Data Source:**
  - Currently supports only local JSON files. No API integration is implemented.
  
- **No Part-Time or Overlap Handling:**
  - All experience is treated as full-time. Overlaps are not deduplicated.
  
- **Lack of Tests:**
  - Tests were not added due to time limitations and need to be introduced later.

## TODO (For Future Work)

- [TODO list](TODO.md)
