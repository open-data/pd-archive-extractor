import click
import tarfile
import os
import sys

if str is bytes:
    #py2
    import unicodecsv as csv
    from StringIO import StringIO
else:
    #py3
    import csv
    from io import StringIO


def clear_stream(stream):
    # type: (StringIO) -> None
    stream.seek(0)
    stream.truncate(0)


def error_message(message):
    # type: (str) -> None
    click.echo("\n\033[1;33m%s\033[0;0m\n" % message, err=True)


def success_message(message):
    # type: (str) -> None
    click.echo("\n\033[0;36m\033[1m%s\033[0;0m\n" % message, err=True)


def recombinant_type(members, type):
    csv = None
    for tarinfo in members:
         if os.path.splitext(tarinfo.name)[0] == type:
             csv = tarinfo
    if csv:
        yield csv
    else:
        raise Exception('Recombinant type %s not in TAR backup.' % type)


@click.command(short_help="Extracts rows for a given Recombinant Type and Organization.")
@click.option('-t', '--type', required=True, type=click.STRING, help='The Recombinant type to extract rows for.')
@click.option('-o', '--org', required=True, type=click.STRING, help='The Organization to extract rows for.')
@click.option('-I', '--input', required=True, type=click.File('r'), help='The TAR backup file to extract from.')
@click.option('-O', '--output', type=click.File('w'), help='The output file path. Otherwise stdout will be used.')
@click.option('-v', '--verbose', is_flag=True, type=click.BOOL, help='Increase verbosity.')
def extract_rows(type=None, org=None, input=None, output=None, verbose=False):

    if output and not output.name.endswith('.csv'):
        error_message('Output file %s must be a CSV file.' % output.name)
        return
    
    if input and (not input.name.endswith('.tar') and not input.name.endswith('.tar.gz')):
        error_message('Input file %s must be a TAR or TARGZ file.' % input.name)
        return

    extracted_stream = StringIO()

    success_message('Looking through %s for %s.csv' % (input.name, type))

    with tarfile.open(input.name) as tar:
        try:
            tar.extractall(path=extracted_stream, members=recombinant_type(tar, type))
        except Exception as e:
            error_message(e)
            clear_stream(extracted_stream)
            return

    if not extracted_stream:
        error_message('Could not the extracted %s.csv after all...' % type)
        clear_stream(extracted_stream)
        return

    success_message('Looking for rows owned by %s. This might take a while...' % org)
    headers = []
    rows = []
    extracted_stream.seek(0)
    with extracted_stream.read() as f:
        try:
            reader = csv.DictReader(f)
            headers = reader.fieldnames
            for row in reader:
                if row['owner_org'] != org:
                    continue
                rows.append(row)
        except Exception as e:
            error_message('Failed to parse rows from csv.')
            clear_stream(extracted_stream)
            return

    if output and rows and headers:
        success_message('Found %s rows owned by %s.' % (len(rows), org))
        success_message('Writing data to %s' % output.name)
        try:
            with open(output.name, 'w') as f:
                writer = csv.DictWriter(f, fieldnames=headers)
                writer.writeheader()
                writer.writerows(rows)
        except Exception as e:
            error_message('Failed to write to output file %s' % output.name)
            clear_stream(extracted_stream)
            return
    elif rows and headers:
        success_message('Found %s rows owned by %s.' % (len(rows), org))
        try:
            writer = csv.DictWriter(sys.stdout, fieldnames=headers)
            writer.writeheader()
            writer.writerows(rows)
        except Exception as e:
            error_message('Failed to write to stdout')
            clear_stream(extracted_stream)
            return
    else:
        error_message('Found %s rows owned by %s.' % (len(rows), org))

    clear_stream(extracted_stream)
