import argparse
from test_selenium import LibraryBooking

def main():
    parser = argparse.ArgumentParser(description="EdUHK Library Booking CLI")
    
    parser.add_argument('-u', '--username', 
                        help='EdUHK Network Username', 
                        required=True)
    parser.add_argument('-p', '--password', 
                        help='EdUHK Network Password', 
                        required=True)
    parser.add_argument('-a', '--area', 
                        help='Booking Area (default: G/F Computer Zone)', 
                        default='gf_computer_zone')
    parser.add_argument('--dry-run', 
                        action='store_true', 
                        help='Simulate booking without actual booking')
    
    args = parser.parse_args()
    
    print("EdUHK Library Booking System")
    print("----------------------------")
    
    booking = LibraryBooking(args.username, args.password)
    
    try:
        # Login
        if booking.login():
            print(f"Attempting to book seat in {args.area}")
            
            if not args.dry_run:
                booking.book_gf_computer_zone()
            else:
                print("[DRY RUN] Booking simulation completed")
    
    except Exception as e:
        print(f"Booking failed: {e}")
    
    finally:
        booking.close()

if __name__ == "__main__":
    main()


"""
If you forget your EdUHK Network Password, please contact "https://www.eduhk.hk/ocio/contact-us" for assistance.
"""