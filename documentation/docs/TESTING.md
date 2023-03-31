
# Rescala - Testing
## Automated Testing

### Python Testing

Unittest

No testing on AllAuth Forms



## Manual Testing

### General
|User Action  | Expected Result  | Pass / Fail |
|--|--|--|
|Navigate to page that doesn't exists  | 404 page is rendered  | Pass |

### Header

|User Action  | Expected Result  | Pass / Fail |
|--|--|--|
| Click R logo | Redirects to Landing Page (unauthenticated) or Dashboard (authenticated)  | Pass |
|Click Sign In | Redirects to Sign In Page  | Pass|
|Click Register  | Redirects to Register Page  | Pass |
|Click Resources | Redirects to Resources Page  | Pass |
|Click Log Practice | Redirects to Log Practice Page |Pass |
|Click Dashboard | Redirects to Dashboard Page  |Pass |

### Footer

|User Action  | Expected Result  | Pass / Fail |
|--|--|--|
|Click GitHub logo | Opens new tab and directs to developer's GitHub page  | Pass |
|Click LinkedIn logo | Opens new tab and directs to developer's Linked page | Pass |

### Landing Page

|User Action  | Expected Result  | Pass / Fail |
|--|--|--|
|Click 'Try Rescala Now' button | Redirects to Register Page  |Pass |

### Sign In Page

|User Action  | Expected Result  | Pass / Fail |
|--|--|--|
|Enter Text Into Input | Floating labels shrink  | Pass |
|Enter Text Into Password Input | Password is obfuscated  | Pass |
|Click Sign In Button with Incomplete Form | Error message(s) appear on form |Pass |
|Click Register Now Button  | Redirects to Register page  |Pass |
| Incorrect Password/Username are submitted  | Error message is rendered  | Pass |
|Correct Passwork & Username  | User is authenticated. Redirects to Dashboard  |Pass |

### Dashboard

|User Action  | Expected Result  | Pass / Fail |
|--|--|--|
|Click on Session in Recent Practice  | Redirects to Session Details Page  | Pass |
|Click on Resource in My Resources  | Redirects to Resource Page | Pass |
|Resize Browser Window  | Widgets optimize masonry layout  | Pass** |
|Hover on circle in Last 30 Days widget | Tool tip shows date | Pass |

** Occassionally on the initial load the Focus chart is overlapping. This is due to the image loading after the layout is complete and needs further investigation.

### My Goals

|User Action  | Expected Result  | Pass / Fail |
|--|--|--|
|Click Add Goal Button  | Modal, with Add Goal Form, opens  |Pass |
|Submit Blank String in the Add Goal Form  | Redirects to Dashboard, renders Error  | Pass |
|Submit Valid Goal  | New Goal is rendered to Dashboard with an empty progress bar  | Pass |
|Click 'X' Button  | Hide Edit Button, Reveal Trash Can Button and Check Button  | Pass |
|Click 'Trash Can' Button  | Removes Goal, redirects to Dashboard, renders confirmation message  |Pass |
|Click 'X' Button, then Check Button  | Return to unchanged Dashboard  | Pass |
|Click 'Pencil' Button  | Hide 'X' Button, Reveal 'Check Button', Reveal Range Input| Pass |
| Click 'Pencil' Button then Check '  |Reveals Spinner, Updates Goal progress, rerenders Dashboard with updated Goal. Renders confirmation message.  |Pass |

### Log Practice

|User Action  | Expected Result  | Pass / Fail |
|--|--|--|
| Submit form with missing required field (Headline, Date, Duration, Reflections)  | Error messages rendered to form  | Pass |
| Submit form with required fields  | Redirects to Dashboard - logged practice is visible on Dashboard. Widgets update with new minute tally and adjusted focus and moods.  | Pass |
|Submit form with no Focus and/or Mood  | Form submits  | Pass |


### View Practice

|User Action  | Expected Result  | Pass / Fail |
|--|--|--|
| User loads page | Correct session is rendered. Moods and Focus, if present, are displayed  | Pass |
|Click Edit Practice Button  | Redirects to Edit Practice Page  | Pass |
|Click Delete Practice Button  | Opens Delete Practice Modal  | Pass |
|Click Close Button in Modal  | Closes Modal  | Pass |
|Confirm Delete Pracitce  | Redirects to Dashboard. Practice is no longer visible on Dashboard  | Pass |

### Edit Practice

|User Action  | Expected Result  | Pass / Fail |
|--|--|--|
| User loads page | Edit Practice form is populated with session  | Pass |
| Submit form with missing required field (Headline, Date, Duration, Reflections)  | Error messages rendered to form  | Pass |
| Submit valid form  | Redirects to View Practice Page. Success message renderes  | Pass |

### Resources

|User Action  | Expected Result  | Pass / Fail |
|--|--|--|
|Hovers on image  | Excerpt overlay displays  | Pass |
|Clicks card  | Redirects to Resource page  | Pass |
| Clicks pagination control  | Redirects forwards or backwards  | Pass |

### Resource

|User Action  | Expected Result  | Pass / Fail |
|--|--|--|
| Authenticated user clicks empty star  | Resource is added to Profile, success message renders  | Pass |
| Authenticated user clicks empty star  | Resource is removed from Profile, success message renders  | Pass |
| Click card recommended card | Redirects to Resource page  | Pass |

### Logout

|User Action  | Expected Result  | Pass / Fail |
|--|--|--|
|Click 'No' Button  |Redirects to Dashboard  | Pass |
|Click 'Yes' button  |Logs user out, redirects to Landing Page  | Pass |


## Bugs

## Validators

## Accessibility

## Lighthouse

## Responsiveness

