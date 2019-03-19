import markdown as markdown_parser
import html as html_parser

from django.core.paginator import Paginator, EmptyPage
from xml.etree.ElementTree import Element

from .exceptions import XmlElementNotFound, XmlElementNotUnique

def str_to_bool(string: str, strict=True) -> bool:
    '''Parses the strings 'true' or 'false' to a boolean.

    The strings are not case sensitive.

    Arguments:

        string: The string to be parsed.

        strict: If True, only 'true' and 'false' will be parsed, 
                with other strings raising a ValueError.
                If False, 'true' will return True and other strings
                will return False. 
    
    NOTE: This is different from using the bool() function on a string.
          The bool() function returns false for an empty string,
          and returns true otherwise. This function parses the words
          'true' and 'false' into a boolean.'''

    # Use the lower-case version of the string
    string_lowercase = string.lower()

    if string_lowercase == 'true':
        # the string is equal to 'true'
        return True
    else:
        if strict:
            if string_lowercase == 'false':
                # the string is equal to 'false'
                return False
            else:
                # The string is invalid
                raise ValueError(
                    f'The string \'{string}\' is invalid. '
                    'Only \'true\' or \'false\' are valid in strict mode.'
                )
        else:
            # The string does not equal 'true'
            return False

def get_unique_xml_element(scope: Element, element: str) -> Element:
    '''Returns an XML element if it is unique in the current scope.
    Returns an error if it is not unique or was not found.

    Uses defusedxml for parsing.

    Arguments:

        scope: The current XML scope.

        element: The name of the element.

    '''

    # Find all occurances of the specified element
    elements = scope.findall(element)

    if len(elements) == 0:
        # If there are no elements, raise an error.
        raise XmlElementNotFound(f'Could not find the <{element}> element.')
    elif len(elements) > 1:
        # If there is more than one element, raise an error.
        raise XmlElementNotUnique(f'There is more than one <{element}> element.')
    else:
        # Return the element
        return elements[0]
            
def parse_formatting(text: str, html: bool = False, markdown: bool = False) -> str:
    '''Parses formatted text.

    Arguments:

        text: The string to be parsed.

        html: If True, html in the original string will not be escaped.

        markdown: If True, the Markdown syntax will be applied.

    '''

    # Escapes HTML tags if HTML is disabled
    if not html:
        text = html_parser.escape(text)

    # Parses Markdown
    # Places the original text in <p> tags if Markdown is disabled in order
    # to maintain consistancy when the page is displayed.
    if markdown:
        text = markdown_parser.markdown(text)
    else:
        text = '<p>' + text + '</p>'

    return text

def surrounding_pages(paginator: Paginator, page: int, count: int = 3) -> dict:
    '''Calculates the page numbers before and after the current page in a
    paginated view.

    Arguments:

        paginator: The Paginator object.

        page: The current page.

        count: The number of pages in either direction.

    '''

    page = int(page)

    page_numbers = {
        'before': [],
        'after': [],
    }

    # Page numbers before the current page
    for _ in range(count):
        try:
            page_current = paginator.page(page - _)
            page_before = page_current.previous_page_number()
        except EmptyPage:
            break

        # Prepend to the list instead of append
        # Ensures that the page numbers are ordered from smallest to largest
        page_numbers['before'] = [page_before] + page_numbers['before']

    # Page numbers after the current page
    for _ in range(count):
        try:
            page_current = paginator.page(page + _)
            page_after = page_current.next_page_number()
        except EmptyPage:
            break

        page_numbers['after'].append(page_after)

    return page_numbers
