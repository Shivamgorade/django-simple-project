import os
# import pandas as pd
from django.http import JsonResponse
import openpyxl
from django.shortcuts import render, redirect
from django.conf import settings
from datetime import datetime

def form_view(request):
    if request.method == 'POST':
        # Metadata
        date = request.POST.get('date')  # ✅ renamed from 'date_time'
        line_no = request.POST.get('line_no')
        shift = request.POST.get('shift')
        part_no = request.POST.get('part_no')
        part_type = request.POST.get('part_type')
        supervisor = request.POST.get('supervisor')

        # ST-15 Inputs
        dmc_st15 = request.POST.get('st15_dmc_no')
        pos_501 = request.POST.get('POS_501')
        pos_502 = request.POST.get('POS_502')
        visual_staking_hu = request.POST.get('VISUAL_STAKING_HU')

        # ST-20 Inputs
        pos_311 = request.POST.get('pos311')
        pos_312 = request.POST.get('pos312')
        pos_411 = request.POST.get('pos411')
        pos_412 = request.POST.get('pos412')
        pos_531 = request.POST.get('pos531')
        pos_532 = request.POST.get('pos532')
        pos_541 = request.POST.get('pos541')
        pos_542 = request.POST.get('pos542')
        visual_staking_st20 = request.POST.get('visualStakingST20')

        # ST-25 Inputs
        pos_221 = request.POST.get('pos_221')
        visual_cbearing = request.POST.get('visual_cbearing')

        # ST-25 MV Staking
        pos201 = request.POST.get('pos201')
        pos202 = request.POST.get('pos202')
        pos211 = request.POST.get('pos211')
        pos212 = request.POST.get('pos212')
        visualStakingMV = request.POST.get('visualStakingMV')

        # ST-30 Motor Staking
        dmc_st30 = request.POST.get('dmc_st30')
        pos222 = request.POST.get('pos222')
        pos223 = request.POST.get('pos223')
        pos224 = request.POST.get('pos224')
        visual_staking_st30 = request.POST.get('visual_staking_st30')

        # ST-40 Inputs
        pos301 = request.POST.get('pos301')
        pos401 = request.POST.get('pos401')
        visualStakingST40 = request.POST.get('visualStakingST40')

        # ST-45 Inputs
        ecuScrewDamage = request.POST.get('ecuScrewDamage')
        pos231status = request.POST.get('pos231status')
        pos232status = request.POST.get('pos232status')

        # ST-85 Inputs
        ecuHousingDamage = request.POST.get('ecuHousingDamage')

        # LAST CHECKED BY Inputs
        checked_by = request.POST.get('checkedBy')

        # Excel path
        excel_path = os.path.join(settings.BASE_DIR, 'myapp', 'data', 'checksheet_data.xlsx')

        # Create or load workbook
        if os.path.exists(excel_path):
            workbook = openpyxl.load_workbook(excel_path)
            sheet = workbook.active
        else:
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            headers = [
                'DATE', 'LINE NO', 'SHIFT', 'PART NO', 'PART TYPE', 'SUPERVISOR',
                'ST15 DMC', 'POS 501 Depth', 'POS 502 Depth', 'Visual Staking HU (ST-15)',
                'POS 311 Depth', 'POS 312 Depth', 'POS 411 Depth', 'POS 412 Depth',
                'POS 531 Depth', 'POS 532 Depth', 'POS 541 Depth', 'POS 542 Depth',
                'Visual Staking (ST-20)',
                'ST25 DMC', 'Visual – C-Bearing',
                'MV DMC', '201 Depth', '202 Depth', '211 Depth', '212 Depth', 'MV Visual',
                'ST30 DMC', '222 Depth', '223 Depth', '224 Depth', 'Visual Staking (ST-30)',
                '301 Depth', '401 Depth', 'Visual Staking (ST-40)',
                'Pos. 231 Status', 'Pos. 232 Status', 'ECU Screw Head Damage',
                'ECU Housing Damage',
                'Checked By',
            ]
            for col, header in enumerate(headers, start=1):
                sheet.cell(row=3, column=col, value=header)

        # Row data
        row_data = [
            date, line_no, shift, part_no, part_type, supervisor,
            dmc_st15, pos_501, pos_502, visual_staking_hu,
            pos_311, pos_312, pos_411, pos_412,
            pos_531, pos_532, pos_541, pos_542,
            visual_staking_st20,
            pos_221, visual_cbearing,
            pos201, pos202, pos211, pos212, visualStakingMV,
            dmc_st30, pos222, pos223, pos224, visual_staking_st30,
            pos301, pos401, visualStakingST40,
            pos231status, pos232status, ecuScrewDamage,
            ecuHousingDamage,
            checked_by,
        ]

        # Find next available row
        next_row = 4
        while sheet.cell(row=next_row, column=1).value:
            next_row += 1

        for col, value in enumerate(row_data, start=1):
            sheet.cell(row=next_row, column=col, value=value)

        workbook.save(excel_path)
        return redirect('form_view')

    return render(request, 'form.html')


def dashboard_view(request):
    return render(request, 'dashboard.html')


# def get_filtered_chart_data(request):
#     try:
#         import os
#         import traceback
#         import pandas as pd
#         from django.http import JsonResponse
#         from django.conf import settings

#         # Get query parameters
#         date = request.GET.get('date')        # e.g., '2025-08-03'
#         line_no = request.GET.get('line')     # e.g., '10M LINE#01'
#         shift = request.GET.get('shift')      # e.g., '1st'

#         print("Received filters:")
#         print(f"Date: {date}, Line: {line_no}, Shift: {shift}")

#         # Load Excel file
#         excel_path = os.path.join(settings.BASE_DIR, 'myapp', 'data', 'checksheet_data.xlsx')
#         df = pd.read_excel(excel_path, header=2)

#         # Clean column names
#         df.columns = [str(col).strip() for col in df.columns]

#         # Normalize and clean data
#         df['DATE'] = pd.to_datetime(df['DATE']).dt.date.astype(str)
#         df['LINE NO'] = df['LINE NO'].astype(str).str.strip().str.upper()
#         df['SHIFT'] = df['SHIFT'].astype(str).str.strip().str.lower()

#         # Normalize filter values
#         date = date.strip()
#         line_no = line_no.strip().upper()
#         shift = shift.strip().lower()

#         print("Normalized filters:")
#         print(f"Date: {date}, Line: {line_no}, Shift: {shift}")
#         print("Available LINE NOs:", df['LINE NO'].unique())
#         print("Available SHIFTs:", df['SHIFT'].unique())
#         print("Available DATEs:", df['DATE'].unique())

#         # Filter the data
#         filtered_df = df[
#             (df['DATE'] == date) &
#             (df['LINE NO'] == line_no) &
#             (df['SHIFT'] == shift)
#         ]

#         print("Filtered rows count:", len(filtered_df))

#         if filtered_df.empty:
#             return JsonResponse({'message': 'No data found for given filter!'}, status=404)

#         row = filtered_df.iloc[0]

#         # Initialize lists
#         labels = []
#         data = []

#         # Read values if available and not NaN
#         if '501' in row and pd.notna(row['501']):
#             labels.append('501')
#             data.append(round(float(row['501']), 2))

#         if '502' in row and pd.notna(row['502']):
#             labels.append('502')
#             data.append(round(float(row['502']), 2))

#         # If both missing, return info message
#         if not labels:
#             return JsonResponse({'message': 'No valid depth data for POS 501 or 502'}, status=204)

#         return JsonResponse({
#             'labels': labels,
#             'data': data
#         })

#     except Exception as e:
#         traceback.print_exc()
#         return JsonResponse({'message': f'Internal Server Error: {str(e)}'}, status=500)

